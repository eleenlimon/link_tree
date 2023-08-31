from django.db import models


# Create your models here.
# Class is a table in your db

# Profiles -> Links (need 2 tables)

class Profile(models.Model):
    BG_CHOICES = (
        ('blue', 'Blue'),
        ('green', "Green"),
        ('yellow', 'Yellow'),
    )
    # name, slug (url nick name), bg_color
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    bg_color = models.CharField(max_length=50, choices=BG_CHOICES)

    # bg_choices for user, avoid an error of them inputting something else

    def __str__(self):  # displays better on the admin
        return self.name


class Link(models.Model):
    # text, url, profile association
    text = models.CharField(max_length=100)
    url = models.URLField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="links")  # pass the class, + profile association,

    # on_delete = models.CASCADE --> allows user to delete profile along w/ all the links( if want user to keep the
    # links can change the (.) method

    def __str__(self):
        return f'{self.text} | {self.url}'

'''
 relationships in db:
 -> many to many = user has access to other links vice versa (NO)
 -> one to one = only link ONE to a user profile(NO)---user can have facebook, insta, etc
 -> many to one = one user with many links (yes)
'''
