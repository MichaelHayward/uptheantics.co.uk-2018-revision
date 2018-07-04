import datetime

from django.db import models
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django import forms

from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey

from taggit.models import TaggedItemBase

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from wagtail.snippets.models import register_snippet
from wagtail.snippets.edit_handlers import SnippetChooserPanel

@register_snippet
class BlogAuthor(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ForeignKey(
        "wagtailimages.Image", null=True, blank=True,
        on_delete=models.SET_NULL, related_name="+"
    )

    panels = [
        FieldPanel("name"),
        ImageChooserPanel("icon"),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "blog authors"

# Create your models here.
class EventsIndexPage(Page):
    intro = RichTextField(blank=True)

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        eventpages = self.get_children().live().order_by("-first_published_at")
        context["eventpages"] = eventpages
        return context

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
    ]

# Still need to add event image field
class EventPage(Page):
    parent_page_types = ['blog.EventsIndexPage']
    gig_date = models.DateField(default=timezone.now)
    gig_time = models.CharField(default="19:30", max_length=5)
    gig_location = models.CharField(default="Location TBA", max_length=200)
    location_link = models.CharField(max_length=2083, default="https://www.uptheantics.co.uk")
    ticket_link = models.CharField(max_length=2083, default="https://www.uptheantics.co.uk")
    price = models.CharField(max_length=6, default="5")
    intro = models.CharField(max_length=100)
    body = RichTextField(blank=True)
    representative_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )


    search_fields = Page.search_fields + [
        index.SearchField("intro"),
        index.SearchField("body"),
    ]

    content_panels = Page.content_panels + [
        FieldPanel("gig_date"),
        FieldPanel("gig_time"),
        FieldPanel("gig_location"),
        FieldPanel("price"),
        MultiFieldPanel([
            FieldPanel("location_link"),
            FieldPanel("ticket_link"),
        ], heading="Relevant Links"),
        FieldPanel("intro"),
        FieldPanel("body", classname="full"),
        ImageChooserPanel('representative_image'),
    ]

class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        all_posts = self.get_children().live().type(BlogPage).order_by("-first_published_at")
        recent_posts = all_posts[:10]
        context["recent_posts"] = recent_posts
        context["all_posts"] = all_posts
        subpage_types = ["Blog"]
        return context

class BlogArchives(Page):
    def get_context(self, request):
        context = super(BlogArchives, self).get_context(request)

        # Get the full unpaginated listing of resource pages as a queryset -
        blogpages = self.get_siblings(inclusive=False).live().order_by("-first_published_at")[9:]

        paginator = Paginator(blogpages, 10) # Show 5 resources per page

        page = request.GET.get('page')
        try:
            blogpages = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            blogpages = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            blogpages = paginator.page(paginator.num_pages)

        # make the variable 'resources' available on the template
        context['blogpages'] = blogpages

        return context

    def __str__(self):
        return self.name

class BlogPage(Page):
    parent_page_types = ['blog.BlogIndexPage']
    date = models.DateField(default=timezone.now)
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)
    author = models.ForeignKey(
        "blog.BlogAuthor",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    representative_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    search_fields = Page.search_fields + [
        index.SearchField("intro"),
        index.SearchField("body"),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            SnippetChooserPanel("author"),
        ], heading="Blog information"),
        FieldPanel("intro"),
        FieldPanel("body", classname="full"),
        InlinePanel("gallery_images", label="Gallery Images"),
        ImageChooserPanel('representative_image'),
    ]

class BlogPageGalleryImage(Orderable):
    page = ParentalKey(BlogPage, on_delete=models.CASCADE, related_name="gallery_images")
    image = models.ForeignKey(
        "wagtailimages.Image", on_delete=models.CASCADE, related_name="+"
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel("image"),
        FieldPanel("caption")
    ]

class AboutPage(Page):
    date = models.DateField(default=timezone.now)
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)

    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel("date"),
        ], heading="Page information"),
        MultiFieldPanel([
            FieldPanel("intro"),
            FieldPanel("body", classname="full"),
        ], heading="Page Content"),
    ]

    def child_pages(self):
        return AboutPage.objects.live().child_of(self).order_by("title")

# Does this need to take in Page as a param? It's just data being handed to About
class Bio(Page):
    name = models.CharField(max_length=100)
    description = RichTextField(blank=True)
    representative_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    content_panels = Page.content_panels +  [
        MultiFieldPanel([
            FieldPanel("name"),
            FieldPanel("description", classname="full"),
            ImageChooserPanel('representative_image'),
        ], heading="Bio")
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "bios"
