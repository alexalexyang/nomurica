from django.views import generic
from django.core.urlresolvers import reverse, reverse_lazy
from .models import Movies
import random
from .countries import countries
from django.db.models import Q

import psycopg2
from django.template import Context


class MoviesListView(generic.ListView):
    model = Movies

    # def get_queryset(self):
    #     random_countries = []
    #     while len(random_countries) < 20:
    #         country_choice = random.choice(countries)
    #         if country_choice in random_countries:
    #             pass
    #         else:
    #             random_countries.append(country_choice)

        # for i in random_countries:
        #     print(i)
        # print(len(random_countries))

        # print([x for x in random_countries])

        # return Movies.objects.order_by('production_countries', '?')[:10]
        # return Movies.objects.filter(production_countries__in=random_countries).distinct('production_countries')[:10]
        # return Movies.objects.filter(Q(production_countries__in=random_countries) | [Q(production_countries__contains=x) for x in random_countries]).distinct('production_countries')[:10]


        # q = Q()
        # for country in random_countries:
        #     q |= Q(production_countries__icontains = country)
        #
        # return Movies.objects.filter(q).distinct('production_countries')[:10]

    def get_context_data(self, **kwargs):

        import psycopg2
        from .countries import countries
        import random
        from psycopg2 import sql

        connection = psycopg2.connect("dbname='db_nomurica_all_movies' "
                                      "user='alex' "
                                      "host='localhost' "
                                      "password='password'")

        c = connection.cursor()

        random_countries = []

        while len(random_countries) < 10:
            choice = random.choice(countries)
            if choice not in random_countries:
                random_countries.append(choice.lower())
            else:
                pass

        rows_list = []

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

        return {"object_list": rows_list}

    template_name = r"movies_crud/movies_list.html"



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