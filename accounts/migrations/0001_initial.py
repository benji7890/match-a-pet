# Generated by Django 3.1.2 on 2020-11-07 22:09

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, verbose_name="email address"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "is_shelter",
                    models.BooleanField(default=False, verbose_name="shelter status"),
                ),
                (
                    "is_clientuser",
                    models.BooleanField(
                        default=False, verbose_name="clientuser status"
                    ),
                ),
                ("phone", models.CharField(blank=True, max_length=10)),
                ("address", models.CharField(max_length=50)),
                ("city", models.CharField(max_length=50)),
                ("state", models.CharField(max_length=50)),
                ("zip_code", models.CharField(blank=True, max_length=5)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.Group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.Permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="ShelterRegisterData",
            fields=[
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="accounts.user",
                    ),
                ),
                (
                    "shelter_profile_image",
                    models.ImageField(
                        blank=True,
                        default="default.jpg",
                        upload_to="shelter_profile_pics",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UserRegisterData",
            fields=[
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="accounts.user",
                    ),
                ),
                (
                    "user_profile_image",
                    models.ImageField(
                        blank=True, default="default.jpg", upload_to="user_profile_pics"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Pet",
            fields=[
                (
                    "id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="accounts.shelterregisterdata",
                    ),
                ),
                ("pet_name", models.CharField(max_length=80)),
                ("pet_breed", models.CharField(max_length=50)),
                ("pet_age", models.CharField(max_length=10)),
                ("pet_color", models.CharField(max_length=50)),
                ("pet_gender", models.CharField(max_length=50)),
                (
                    "pet_profile_image1",
                    models.ImageField(
                        blank=True, default="default.jpg", upload_to="pet_profile_pics"
                    ),
                ),
                (
                    "pet_image_url",
                    models.URLField(
                        blank=True,
                        default="https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/48212723/1/?bust=1592050579&width=450",
                        max_length=250,
                    ),
                ),
                (
                    "pet_profile_image2",
                    models.ImageField(
                        blank=True, default="default.jpg", upload_to="pet_profile_pics"
                    ),
                ),
                (
                    "pet_profile_image3",
                    models.ImageField(
                        blank=True, default="default.jpg", upload_to="pet_profile_pics"
                    ),
                ),
            ],
        ),
    ]
