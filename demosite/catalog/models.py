from django.db import models
# Used to generate URLs by reversing the URL patterns
from django.urls import reverse
# Required for unique book instances
import uuid

# Create your models here.

# django will assign primary key automatically if
# not specified by primary_key=True for some field, but I want
# to put it in myself for visual reasons:
# id = models.BigAutoField(primary_key=True)

class Style(models.Model):
    """Model representing a dance style."""
    # id automatic
    name = models.CharField(max_length=200, help_text='Enter a dance style (e.g. Salsa)')
    PARTNER_STRUCTURE = (
        ('s', 'solo dance'),
        ('p', 'partnered'),
    )

    partner_needed = models.CharField(
        max_length=1,
        choices=PARTNER_STRUCTURE,
        blank=True,
        default='p',
        help_text='enter whether this is a pair dance with partner (e.g. Ballroom) or a solo dance (e.g. Hip hop)',
    )

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Language(models.Model):
    """Model representing a spoken language."""
    # id automatic
    name = models.CharField(max_length=200, help_text='Enter a language (e.g. French)')

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Dance_course(models.Model):
    """Model representing a dance course (but not a specific copy instance of a dance course)."""

    #id automatic
    title = models.CharField(max_length=200)

    '''not needed for my class: foreign key
    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author is a string rather than an object because it hasn't been declared yet in the file
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    '''

    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the dance course')
    ''' not needed
    isbn = models.CharField('ISBN', max_length=13, unique=True,
                             help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    '''

    ''' many to many
    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    # Genre class has already been defined so we can specify the object above.
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')
    '''
    # TODO change to object
    style = models.ForeignKey('Style', on_delete=models.SET_NULL, null=True)

    #TODO LANGUAGE

    cost = models.DecimalField(max_digits=5, decimal_places=2)


    def __str__(self):
        """String for representing the Model object."""
        return self.title

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this dance course."""
        return reverse('dance_course-detail', args=[str(self.id)])



class Dance_course_instance(models.Model):
    """Model representing a specific instance of a dance course (i.e. that took place in one semester)."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular run of a specific dance course e.g. in one particular semester')
    dance_course = models.ForeignKey('Dance_course', on_delete=models.RESTRICT, null=True)
    start_date = models.DateField(null=True, blank=True)

    DAYS = (
        ('mo', 'Monday'),
        ('tu', 'Tuesday'),
        ('we', 'Wednesday'),
        ('th', 'Thursday'),
        ('fr', 'Friday'),
        ('sa', 'Saturday'),
        ('su', 'Sunday'),
    )

    day = models.CharField(
        max_length=2,
        choices=DAYS,
        blank=True,
        default='mo',
        help_text= 'On which day is the course?'
    )

    time = models.CharField(max_length=5, blank=True)

    RUN_STATUS = (
        ('f', 'Finished'),
        ('o', 'Ongoing currently'),
        ('n', 'not yet started'),
    )

    running = models.CharField(
        max_length=1,
        choices=RUN_STATUS,
        blank=True,
        default='n',
        help_text='Is the course currently running, finished in the past or will start to be held in the future',
    )

    instructor = models.ManyToManyField('Instructor', help_text='Select instructor(s) for this dance course instance')

    # TODO spot,  max_size, attending_students

    class Meta:
        ordering = ['start_date']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.book.title})'



class Instructor(models.Model):
    """Model representing a dance instructor."""

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    speaks_language = models.ManyToManyField(Language, help_text='Select language(s) the instructor can teach in')


    class Meta:
        ordering = ['first_name', 'last_name']

    def get_absolute_url(self):
        """Returns the URL to access a particular instructor instance."""
        return reverse('instructor-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'
