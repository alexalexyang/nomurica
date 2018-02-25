from django import forms

GENRE_CHOICES = (
    ('Romance', 'Romance'),
    ('Action', 'Action'),
    ('Drama', 'Drama'),
    ('Documentary', 'Documentary'),
    ('Crime', 'Crime'),
    ('Horror', 'Horror'),
    ('Comedy', 'Comedy'),
    ('Animation', 'Animation'),
    ('Thriller', 'Thriller'),
    ('Family', 'Family'),
    ('Fantasy', 'Fantasy'),
    ('Foreign', 'Foreign'),
    ('Music', 'Music'),
    ('Adventure', 'Adventure'),
    ('War', 'War'),
    ('Science Fiction', 'Science Fiction'),
    ('Mystery', 'Mystery'),
    ('History', 'History'),
    ('Western', 'Western'),
    ('TV Movie', 'TV Movie'),
)
class GenresForm(forms.Form):

    genres = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=GENRE_CHOICES)