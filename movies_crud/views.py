from django.shortcuts import render, redirect
from django.views import generic
from .models import Movies
import psycopg2
import random
from .countries import countries
from .forms import GenresForm
from django.core.urlresolvers import reverse, reverse_lazy

def Movies(request):

    # Create cursor for database.

    connection = psycopg2.connect("dbname='db_nomurica_all_movies' "
                                  "user='alex' "
                                  "host='localhost' "
                                  "password='password'")

    c = connection.cursor()

    # rows_list will become the context.
    rows_list = []
    form = GenresForm(request.POST)

    if request.method == 'POST':

        if form.is_valid():
            genres = form.cleaned_data.get('genres')

            while len(rows_list) < 10:

                random_countries = []
                while len(random_countries) < 10:
                    choice = random.choice(countries)
                    if choice not in random_countries:
                        random_countries.append(choice.lower())
                    else:
                        pass

                # Get the movies based on the country and return them as a Django context.
                for country in random_countries:
                    get_rows = "SELECT * FROM movies_nonhegemony WHERE LOWER(production_countries) LIKE %s AND genres = ALL(%s) LIMIT 1;"
                    c.execute(get_rows, ('%' + country + '%', genres,))
                    rows = c.fetchall()

                    rows_list_titles = []
                    for i in rows_list:
                        rows_list_titles.append(i['title'])

                    for i in rows:
                        if i[4] not in rows_list_titles:
                            row_dict = {}
                            row_dict['id'] = i[0]
                            row_dict['adult'] = i[1]
                            row_dict['original_language'] = i[2]
                            row_dict['original_title'] = i[3]
                            row_dict['title'] = i[4]
                            row_dict['overview'] = i[5]
                            row_dict['release_date'] = i[6]
                            row_dict['genres'] = i[7]
                            row_dict['production_countries'] = i[8]
                            row_dict['videos'] = i[9]
                            row_dict['images'] = i[10]
                            rows_list.append(row_dict)
                            print(i[7])

                if len(rows_list) < 10:
                    need_more_rows = 10 - len(rows_list)

                    additional_random_countries = []
                    while len(additional_random_countries) < need_more_rows:
                        choice = random.choice(countries)
                        if choice not in additional_random_countries and choice not in random_countries:
                            additional_random_countries.append(choice.lower())
                        else:
                            pass

                    for country in additional_random_countries:
                        get_rows = "SELECT * FROM movies_nonhegemony WHERE LOWER(production_countries) LIKE %s AND genres = ANY(%s) LIMIT 1;"
                        c.execute(get_rows, ('%' + country + '%', genres,))

                        rows_additional = c.fetchall()

                        rows_list_titles = []
                        for i in rows_list:
                            rows_list_titles.append(i['title'])

                        for i in rows_additional:
                            if i[4] not in rows_list_titles:
                                row_dict = {}
                                row_dict['id'] = i[0]
                                row_dict['adult'] = i[1]
                                row_dict['original_language'] = i[2]
                                row_dict['original_title'] = i[3]
                                row_dict['title'] = i[4]
                                row_dict['overview'] = i[5]
                                row_dict['release_date'] = i[6]
                                row_dict['genres'] = i[7]
                                row_dict['production_countries'] = i[8]
                                row_dict['videos'] = i[9]
                                row_dict['images'] = i[10]
                                rows_list.append(row_dict)
            print(len(rows_list))

        else:
            return redirect('/crud/movies/')

    else:

        # Acquire 10 random countries from the full list.
        random_countries = []

        while len(random_countries) < 10:
            choice = random.choice(countries)
            if choice not in random_countries:
                random_countries.append(choice.lower())
            else:
                pass

        # Get the movies based on the country and return them as a Django context.
        for country in random_countries:
            get_rows = "SELECT * FROM movies_nonhegemony WHERE LOWER(production_countries) LIKE %s LIMIT 1;"
            c.execute(get_rows, ('%' + country + '%',))

            rows = c.fetchall()

            for i in rows:
                row_dict = {}
                row_dict['id'] = i[0]
                row_dict['adult'] = i[1]
                row_dict['original_language'] = i[2]
                row_dict['original_title'] = i[3]
                row_dict['title'] = i[4]
                row_dict['overview'] = i[5]
                row_dict['release_date'] = i[6]
                row_dict['genres'] = i[7]
                row_dict['production_countries'] = i[8]
                row_dict['videos'] = i[9]
                row_dict['images'] = i[10]
                rows_list.append(row_dict)

    connection.close()

    return render(request, r"movies_crud/movies_list.html", {"object_list": rows_list, "form": form})



# def GenresView(request):
#     if request.method == 'POST':
#         form = GenresForm(request.POST)
#         if form.is_valid():
#             genres = form.cleaned_data.get('genres')
#             print(genres)
#     else:
#         form = GenresForm
#
#     return render(request, r"movies_crud/genres_form.html", {'form':form})


# class MoviesListView(generic.ListView):
#     model = Movies
#
#     def get_context_data(self, **kwargs):
#
#         # Create cursor for database.
#
#         connection = psycopg2.connect("dbname='db_nomurica_all_movies' "
#                                       "user='alex' "
#                                       "host='localhost' "
#                                       "password='password'")
#
#         c = connection.cursor()
#
#         # Acquire 10 random countries from the full list.
#         random_countries = []
#
#         while len(random_countries) < 10:
#             choice = random.choice(countries)
#             if choice not in random_countries:
#                 random_countries.append(choice.lower())
#             else:
#                 pass
#
#         # Get the movies based on the country and return them as a Django context.
#
#         rows_list = []
#
#         for country in random_countries:
#
#             get_rows = "SELECT * FROM movies_nonhegemony WHERE LOWER(production_countries) LIKE %s LIMIT 1;"
#
#             c.execute(get_rows, ('%' + country + '%',))
#             rows = c.fetchall()
#
#             for i in rows:
#                 row_dict = {}
#                 row_dict['id'] = i[0]
#                 row_dict['adult'] = i[1]
#                 row_dict['original_language'] = i[2]
#                 row_dict['original_title'] = i[3]
#                 row_dict['title'] = i[4]
#                 row_dict['overview'] = i[5]
#                 row_dict['release_date'] = i[6]
#                 row_dict['genres'] = i[7]
#                 row_dict['production_countries'] = i[8]
#                 row_dict['videos'] = i[9]
#                 row_dict['images'] = i[10]
#                 rows_list.append(row_dict)
#
#         connection.close()
#         return {"object_list": rows_list}
#
#     template_name = r"movies_crud/movies_list.html"



# class MoviesCreateView(generic.CreateView):
#     model = Movies
#
#     fields = [
#         'project_name',
#         'artists',
#         'production_countries',
#         'overview',
#         'start_date',
#         'end_date',
#         'medium',
#         'videos',
#         'images',
#         'website',
#         'facebook',
#         'twitter',
#         'other_social_media',
#               ]
#
#     template_name = r"movies_crud/movies_form.html"
#
#     def get_success_url(self):
#         return reverse('movies list')
#
#
# class MoviesDetailView(generic.DetailView):
#     model = Movies
#
#     template_name = r"movies_crud/movies_detail.html"
#
#
# class MoviesUpdateView(generic.UpdateView):
#     model = Movies
#
#     fields = [
#         'project_name',
#         'artists',
#         'production_countries',
#         'overview',
#         'start_date',
#         'end_date',
#         'medium',
#         'videos',
#         'images',
#         'website',
#         'facebook',
#         'twitter',
#         'other_social_media',
#               ]
#
#     # template_name = r"movies_crud/movies_update.html"
#
#
# class MoviesDeleteView(generic.DeleteView):
#     model = Movies
#
#     success_url = reverse_lazy('movies list')