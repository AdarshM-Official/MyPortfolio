from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    short_description = models.CharField(max_length=250)
    description = models.TextField()

    image = models.ImageField(upload_to="projects/")
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)

    technologies = models.CharField(
        max_length=300,
        help_text="Comma separated values"
    )

    featured = models.BooleanField(default=False)
    display_order = models.PositiveIntegerField(default=0)

    created_at = models.DateField()
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["display_order"]
    
    @property
    def tech_list(self):
        return [t.strip() for t in self.technologies.split(",")]
    
    def __str__(self):
        return self.title
    
class Experience(models.Model):
    company = models.CharField(max_length=200)
    position = models.CharField(max_length=200)

    start_date = models.DateField()
    end_date = models.DateField(
        blank=True,
        null=True
    )

    currently_working = models.BooleanField(default=False)

    description = models.TextField()

    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["display_order"]

    def __str__(self):
        return f"{self.position} - {self.company}"
    
class Education(models.Model):
    institution = models.CharField(max_length=250)
    degree = models.CharField(max_length=250)

    start_year = models.PositiveIntegerField()
    end_year = models.PositiveIntegerField()

    description = models.TextField(blank=True)

    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["display_order"]

    def __str__(self):
        return self.degree
    
class Skill(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(
        max_length=100,
        blank=True,
        help_text="FontAwesome class"
    )

    category = models.CharField(
        max_length=100,
        choices=[
            ("frontend", "Frontend"),
            ("backend", "Backend"),
            ("database", "Database"),
            ("ai", "AI"),
            ("tools", "Tools"),
        ]
    )

    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["display_order"]

    def __str__(self):
        return self.name
    
class Service(models.Model):
    title = models.CharField(max_length=200)
    icon = models.CharField(max_length=100)
    description = models.TextField()

    featured = models.BooleanField(default=False)

    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["display_order"]

    def __str__(self):
        return self.title