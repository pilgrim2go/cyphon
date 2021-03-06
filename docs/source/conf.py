#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Cyphon documentation build configuration file, created by
# sphinx-quickstart on Tue Feb  2 12:56:39 2016.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# from __future__ import absolute_import, unicode_literals

import sys
import os
try:
    from unittest.mock import MagicMock
except ImportError:
    from mock import MagicMock


class Mock(MagicMock):

    @classmethod
    def __getattr__(cls, name):
        if name == 'default_app_config':
            raise AttributeError()
        return MagicMock()


def make_mock(mod_name, *args, **kwargs):
    mock = Mock(*args, **kwargs)
    mock.__name__ = ''
    mock.__path__ = []
    mock.__file__ = ''
    return mock


MOCK_MODULES = [
    'django.contrib.gis',
    'django.contrib.gis.db',
    'django.contrib.gis.db.models',
    'django.contrib.gis.geos',
    'elasticsearch',
]


sys.modules.update((mod_name, make_mock(mod_name)) for mod_name in MOCK_MODULES)

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath('../../cyphon'))

os.environ['DJANGO_SETTINGS_MODULE'] = 'cyphon.settings.sphinx'
import django
django.setup()


import target.locations.models
target.locations.models.Location.objects = MagicMock()

# sys.path.insert(0, os.path.abspath('..'))
# from django.conf import settings
# settings.configure()

# from django.conf import settings

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
# source_suffix = ['.rst', '.md']
source_suffix = '.txt'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'Cyphon'
copyright = '2017 Dunbar Security Solutions, Inc.'
author = 'Leila Hadj-Chikh'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '1.5'
# The full version, including alpha/beta/rc tags.
release = '1.5.3'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = [
    '**tests**',
    '**migrations**',
    'figures/*',
    'summaries/*',
]

# The reST default role (used for this markup: `text`) to use for all
# documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'trac'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = '_static/images/favicon.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

html_scaled_image_link = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'h', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'r', 'sv', 'tr'
#html_search_language = 'en'

# A dictionary with options for the search language support, empty by default.
# Now only 'ja' uses this config value
#html_search_options = {'type': 'default'}

# The name of a javascript file (relative to the configuration directory) that
# implements a search results scorer. If empty, the default will be used.
#html_search_scorer = 'scorer.js'

# Output file base name for HTML help builder.
htmlhelp_basename = 'cyphondoc'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',

# Latex figure (float) alignment
#'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'Cyphon.tex', 'Cyphon Documentation',
     'Dunbar Security Solutions', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'cyphon', 'Cyphon Documentation', [author], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'Cyphon', 'Cyphon Documentation', author, 'Cyphon',
     'Incident Management and Response Platform', 'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False


# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    'formtools': ('http://django-formtools.readthedocs.io/en/latest/', None),
    'django': ('https://docs.djangoproject.com/en/1.10/',
               'https://docs.djangoproject.com/en/1.10/_objects/'),
    'elasticsearch': ('https://elasticsearch-py.readthedocs.io/en/5.0.1/',
                      None),
    'mongodb': ('http://api.mongodb.com/python/current/', None),
    'numpy': ('https://docs.scipy.org/doc/numpy/', None),
    'psycopg2': ('http://initd.org/psycopg/docs/', None),
    'python': ('https://docs.python.org/3/', None),
    'six': ('https://pythonhosted.org/six/', None),
    'sphinx': ('http://www.sphinx-doc.org/en/stable/', None),
}

rst_epilog = """
.. _Auth: https://docs.djangoproject.com/en/1.10/topics/auth/
.. _cleaning and validating: https://docs.djangoproject.com/en/1.10/ref/forms/validation/#cleaning-and-validating-fields-that-depend-on-each-other
.. _custom filtering: http://www.django-rest-framework.org/api-guide/filtering/#custom-generic-filtering
.. _Cyphondock: https://github.com/dunbarcyber/cyphondock
.. _Elasticsearch: https://www.elastic.co/products/elasticsearch/
.. _Django: https://www.djangoproject.com/
.. _Django admin site: https://docs.djangoproject.com/en/1.10/ref/contrib/admin/#module-django.contrib.admin
.. _Django Mailbox: http://django-mailbox.readthedocs.io/en/latest/
.. _Django REST Framework: http://www.django-rest-framework.org/
.. _Docker: https://www.docker.com/
.. _Filebeat: https://www.elastic.co/products/beats/filebeat/
.. _FilterSet: http://django-filter.readthedocs.io/en/develop/ref/filterset.html
.. _format codes: http://strftime.org/
.. _Generic Relations: http://docs.djangoproject.com/en/1.10/ref/contrib/contenttypes/#generic-relations
.. _Groups: https://docs.djangoproject.com/en/1.10/topics/auth/default/#groups
.. _Logstash: https://www.elastic.co/products/logstash/
.. _ModelViewSet: http://www.django-rest-framework.org/api-guide/viewsets/#modelviewset
.. _modify an initial queryset: https://docs.djangoproject.com/en/1.10/topics/db/managers/#modifying-a-manager-s-initial-queryset
.. _MongoDB: https://www.mongodb.com/
.. _PostgreSQL: https://www.postgresql.org/
.. _RabbitMQ: https://www.rabbitmq.com/
.. _select related: https://docs.djangoproject.com/en/1.10/ref/models/querysets/#select-related
.. _Signals: https://docs.djangoproject.com/en/1.10/topics/signals/
.. _PageNumberPagination: http://www.django-rest-framework.org/api-guide/pagination/#pagenumberpagination
.. _ReadOnlyModelViewSet: http://www.django-rest-framework.org/api-guide/viewsets/#readonlymodelviewset
.. _Request: http://www.django-rest-framework.org/api-guide/requests/#requests
.. _Response: http://www.django-rest-framework.org/api-guide/responses/#response
.. |bool| replace:: :class:`bool`
.. |datetime| replace:: :class:`~datetime.datetime`
.. |dict| replace:: :class:`dict`
.. |False| replace:: :obj:`False`
.. |float| replace:: :class:`float`
.. |int| replace:: :class:`int`
.. |list| replace:: :class:`list`
.. |object| replace:: :class:`object`
.. |Message| replace:: :py:class:`~Message`
.. |None| replace:: :obj:`None`
.. |NotImplemented| replace:: :obj:`NotImplemented`
.. |NotImplementedError| replace:: :class:`NotImplementedError`
.. |ObjectId| replace:: :class:`~bson.objectid.ObjectId`
.. |ObjectIds| replace:: :class:`ObjectIds<bson.objectid.ObjectId>`
.. |str| replace:: :class:`str`
.. |True| replace:: :obj:`True`
.. |tuple| replace:: :class:`tuple`
.. |type| replace:: :class:`type`
.. |AppConfig| replace:: :class:`~django.apps.AppConfig`
.. |Elasticsearch| replace:: :class:`~elasticsearch.Elasticsearch`
.. |Field| replace:: :class:`~django:django.db.models.Field`
.. |Fields| replace:: :class:`Fields<django:django.db.models.Field>`
.. |ForeignKey| replace:: :class:`~django:django.db.models.ForeignKey`
.. |GenericForeignKey| replace:: :class:`~django:django.contrib.contenttypes.fields.GenericForeignKey`
.. |Group| replace:: :class:`~django:django.contrib.auth.models.Group`
.. |Groups| replace:: :class:`Groups<django:django.contrib.auth.models.Group>`
.. |JSONField| replace:: :class:`~django.contrib.postgres.fields.JSONField`
.. |Manager| replace:: :class:`~django:django.db.models.Manager`
.. |ManyToManyField| replace:: :class:`~django:django.db.models.ManyToManyField`
.. |Model| replace:: :class:`~django:django.db.models.Model`
.. |Models| replace:: :class:`Models<django:django.db.models.Model>`
.. |ModelAdmin| replace:: :class:`~django.contrib.admin.ModelAdmin`
.. |OneToOneField| replace:: :class:`~django:django.db.models.OneToOneField`
.. |Point| replace:: :class:`~from django.contrib.gis.geos.Point`
.. |QuerySet| replace:: :class:`~django:django.db.models.query.QuerySet`
.. |Signal| replace:: :class:`~django.dispatch.Signal`
.. |User| replace:: :class:`~django:django.contrib.auth.models.User`
.. |Users| replace:: :class:`Users<django:django.contrib.auth.models.User>`
.. |Aggregator| replace:: :ref:`Aggregator<aggregator>`
.. |Ambassador| replace:: :ref:`Ambassador<ambassador>`
.. |AppUser| replace:: :class:`~appusers.models.AppUser`
.. |AppUsers| replace:: :class:`AppUsers<appusers.models.AppUser>`
.. |Account| replace:: :class:`~target.followees.models.Account`
.. |Accounts| replace:: :class:`Accounts<target.followees.models.Account>`
.. |Action| replace:: :class:`~responder.actions.models.Action`
.. |Actions| replace:: :class:`Actions<responder.actions.models.Action>`
.. |Alarm| replace:: :class:`~alarms.models.Alarm`
.. |Alarms| replace:: :class:`Alarms<alarms.models.Alarm>`
.. |Alias| replace:: :class:`~target.followees.models.Alias`
.. |Aliases| replace:: :class:`Followees<target.followees.models.Alias>`
.. |Alert| replace:: :class:`~alerts.models.Alert`
.. |Alerts| replace:: :class:`Alerts<alerts.models.Alert>`
.. |ALERT_LEVEL_CHOICES| replace:: :const:`~cyphon.choices.ALERT_LEVEL_CHOICES`
.. |Analysis| replace:: :class:`~alerts.models.Analysis`
.. |Analyses| replace:: :class:`Analyses<alerts.models.Analysis>`
.. |Article| replace:: :class:`~articles.models.Article`
.. |Articles| replace:: :class:`Articles<articles.models.Article>`
.. |BACKEND_CHOICES| replace:: :attr:`~engines.registry.BACKEND_CHOICES`
.. |Bottle| replace:: :class:`~bottler.bottles.models.Bottle`
.. |Bottles| replace:: :class:`Bottles<bottler.bottles.models.Bottle>`
.. |BottleField| replace:: :class:`~bottler.bottles.models.BottleField`
.. |BottleFields| replace:: :class:`BottleFields<bottler.bottles.models.BottleField>`
.. |Cargo| replace:: :class:`~ambassador.transport.Cargo`
.. |Cargos| replace:: :class:`Cargos<ambassador.transport.Cargo>`
.. |Carrier| replace:: :class:`~responder.carrier.Carrier`
.. |Carriers| replace:: :class:`Carriers<responder.carrier.Carrier>`
.. |Category| replace:: :class:`~categories.models.Category`
.. |Categories| replace:: :class:`Categories<categories.models.Category>`
.. |CELERYBEAT_SCHEDULE| replace:: :attr:`~cyphon.settings.base.CELERYBEAT_SCHEDULE`
.. |Chute| replace:: :class:`~sifter.chutes.models.Chute`
.. |Chutes| replace:: :class:`Chutes<sifter.chutes.models.Chute>`
.. |CodeBook| replace:: :class:`~codebooks.models.CodeBook`
.. |CodeBooks| replace:: :class:`CodeBooks<codebooks.models.CodeBook>`
.. |CodeName| replace:: :class:`~codebooks.models.CodeName`
.. |CodeNames| replace:: :class:`CodeNames<codebooks.models.CodeName>`
.. |Collection| replace:: :class:`~warehouses.models.Collection`
.. |Collections| replace:: :class:`Collections<warehouses.models.Collection>`
.. |ContentType| replace:: :class:`~django.contrib.contenttypes.models.ContentType`
.. |CollectionQuery| replace:: :class:`~query.collectionqueries.models.CollectionQuery`
.. |CollectionQueries| replace:: :class:`CollectionQueries<query.collectionqueries.models.CollectionQuery>`
.. |Comment| replace:: :class:`~alerts.models.Comment`
.. |Comments| replace:: :class:`Comments<alerts.models.Comment>`
.. |Company| replace:: :class:`~companies.models.Company`
.. |Companies| replace:: :class:`Companies<companies.models.Company>`
.. |Condenser| replace:: :class:`~sifter.condensers.models.Condenser`
.. |Condensers| replace:: :class:`Condensers<sifter.condensers.models.Condenser>`
.. |Container| replace:: :class:`~bottler.containers.models.Container`
.. |Containers| replace:: :class:`Containers<bottler.containers.models.Container>`
.. |Context| replace:: :class:`~contexts.models.Context`
.. |Contexts| replace:: :class:`Contexts<contexts.models.Context>`
.. |ContextFilter| replace:: :class:`~contexts.models.ContextFilter`
.. |ContextFilters| replace:: :class:`Contexts<contexts.models.ContextFilter>`
.. |Courier| replace:: :class:`~responder.couriers.models.Courier`
.. |Couriers| replace:: :class:`Couriers<responder.couriers.models.Courier>`
.. |Alert.data| replace:: :class:`~alerts.models.Alert.data`
.. |DataChute| replace:: :class:`~sifter.datasifter.datachutes.models.DataChute`
.. |DataChutes| replace:: :class:`DataChutes<sifter.datasifter.datachutes.models.DataChute>`
.. |DataCondenser| replace:: :class:`~sifter.datasifter.datacondensers.models.DataCondenser`
.. |DataCondensers| replace:: :class:`DataCondensers<sifter.datasifter.datacondensers.models.DataCondenser>`
.. |DataField| replace:: :class:`~bottler.datafields.models.DataField`
.. |DataFields| replace:: :class:`DataFields<bottler.datafields.models.DataField>`
.. |DataFitting| replace:: :class:`~sifter.datasifter.datacondensers.models.DataFitting`
.. |DataFittings| replace:: :class:`DataFittings<sifter.datasifter.datacondensers.models.DataFitting>`
.. |DataMunger| replace:: :class:`~sifter.datasifter.datamungers.models.DataMunger`
.. |DataMungers| replace:: :class:`DataMungers<sifter.datasifter.datamungers.models.DataMunger>`
.. |DataParser| replace:: :class:`~sifter.datasifter.datacondensers.models.DataParser`
.. |DataParsers| replace:: :class:`DataParsers<sifter.datasifter.datacondensers.models.DataParser>`
.. |DataRule| replace:: :class:`~sifter.datasifter.datasieves.models.DataRule`
.. |DataRules| replace:: :class:`DataRules<sifter.datasifter.datasieves.models.DataRule>`
.. |DataSieve| replace:: :class:`~sifter.datasifter.datasieves.models.DataSieve`
.. |DataSieves| replace:: :class:`DataSieves<sifter.datasifter.datasieves.models.DataSieve>`
.. |DataSieveNode| replace:: :class:`~sifter.datasifter.datasieves.models.DataSieveNode`
.. |DataSieveNodes| replace:: :class:`DataSieveNodes<sifter.datasifter.datasieves.models.DataSieveNode>`
.. |DataTagger| replace:: :class:`~tags.models.DataTagger`
.. |DataTaggers| replace:: :class:`DataTaggers<tags.models.DataTagger>`
.. |Destination| replace:: :class:`~responder.destinations.models.Destination`
.. |Destinations| replace:: :class:`Destinations<responder.destinations.models.Destination>`
.. |Dispatch| replace:: :class:`~responder.dispatches.models.Dispatch`
.. |Dispatches| replace:: :class:`Dispatches<responder.dispatches.models.Dispatch>`
.. |Distilleries| replace:: :class:`Distilleries<distilleries.models.Distillery>`
.. |Distillery| replace:: :class:`~distilleries.models.Distillery`
.. |DocumentObj| replace:: :class:`~cyphon.documents.DocumentObj`
.. |document_saved| replace:: :const:`~distilleries.signals.document_saved`
.. |Emissary| replace:: :class:`~ambassador.emissaries.models.Emissary`
.. |Emissaries| replace:: :class:`Emissaries<ambassador.emissaries.models.Emissary>`
.. |Endpoint| replace:: :class:`~ambassador.endpoints.models.Endpoint`
.. |Endpoints| replace:: :class:`Endpoints<ambassador.endpoints.models.Endpoint>`
.. |Engine| replace:: :class:`~engines.engine.Engine`
.. |Engines| replace:: :class:`Engines<engines.engine.Engine>`
.. |Engineer| replace:: :class:`~aggregator.pumproom.engineer.Engineer`
.. |EngineQuery| replace:: :class:`~engines.queries.EngineQuery`
.. |EngineQueries| replace:: :class:`EngineQueries<engines.queries.EngineQuery>`
.. |EngineQueryFieldset| replace:: :class:`~engines.queries.EngineQueryFieldset`
.. |EngineQueryFieldsets| replace:: :class:`EngineQueryFieldsets<engines.queries.EngineQueryFieldset>`
.. |ElasticsearchEngine| replace:: :class:`~engines.elasticsearch.engine.ElasticsearchEngine`
.. |Faucet| replace:: :class:`~aggregator.pumproom.faucet.Faucet`
.. |FIELD_TYPE_CHOICES| replace:: :const:`~cyphon.choices.FIELD_TYPE_CHOICES`
.. |Fieldset| replace:: :class:`~query.collectionqueries.models.Fieldset`
.. |Fieldsets| replace:: :class:`Fieldsets<query.collectionqueries.models.Fieldset>`
.. |Filter| replace:: :class:`~aggregator.filters.models.Filter`
.. |Filters| replace:: :class:`Filters<aggregator.filters.models.Filter>`
.. |Fitting| replace:: :class:`~sifter.condensers.models.Fitting`
.. |Fittings| replace:: :class:`Fittings<sifter.condensers.models.Fitting>`
.. |Followee| replace:: :class:`~target.followees.models.Followee`
.. |Followees| replace:: :class:`Followees<target.followees.models.Followee>`
.. |Funnel| replace:: :class:`~aggregator.funnels.models.Funnel`
.. |Funnels| replace:: :class:`Funnels<aggregator.funnels.models.Funnel>`
.. |GEOCOORDINATE_CHOICES| replace:: :const:`~cyphon.choices.GEOCOORDINATE_CHOICES`
.. |Inspection| replace:: :class:`~inspections.models.Inspection`
.. |Inspections| replace:: :class:`Inspections<inspections.models.Inspection>`
.. |Invoice| replace:: :class:`~aggregator.invoices.models.Invoice`
.. |Invoices| replace:: :class:`Invoices<aggregator.invoices.models.Invoice>`
.. |Label| replace:: :class:`~bottler.labels.models.Label`
.. |Labels| replace:: :class:`Labels<bottler.labels.models.Label>`
.. |LegalName| replace:: :class:`~target.followees.models.LegalName`
.. |Location| replace:: :class:`~target.locations.models.Location`
.. |Locations| replace:: :class:`Locations<target.locations.models.Location>`
.. |LOGIC_CHOICES| replace:: :const:`~cyphon.choices.LOGIC_CHOICES`
.. |LogChute| replace:: :class:`~sifter.logsifter.logchutes.models.LogChute`
.. |LogChutes| replace:: :class:`LogChutes<sifter.logsifter.logchutes.models.LogChute>`
.. |LogCondenser| replace:: :class:`~sifter.logsifter.logcondensers.models.LogCondenser`
.. |LogCondensers| replace:: :class:`LogCondensers<sifter.logsifter.logcondensers.models.LogCondenser>`
.. |LogFitting| replace:: :class:`~sifter.logsifter.logcondensers.models.LogFitting`
.. |LogFittings| replace:: :class:`LogFittings<sifter.logsifter.logcondensers.models.LogFitting>`
.. |LogMunger| replace:: :class:`~sifter.logsifter.logmungers.models.LogMunger`
.. |LogMungers| replace:: :class:`LogMungers<sifter.logsifter.logmungers.models.LogMunger>`
.. |LogParser| replace:: :class:`~sifter.logsifter.logcondensers.models.LogParser`
.. |LogParsers| replace:: :class:`LogParsers<sifter.logsifter.logcondensers.models.LogParser>`
.. |LogRule| replace:: :class:`~sifter.logsifter.logsieves.models.LogRule`
.. |LogRules| replace:: :class:`LogRules<sifter.logsifter.logsieves.models.LogRule>`
.. |LogSieve| replace:: :class:`~sifter.logsifter.logsieves.models.LogSieve`
.. |LogSieves| replace:: :class:`LogSieves<sifter.logsifter.logsieves.models.LogSieve>`
.. |LogSieveNode| replace:: :class:`~sifter.logsifter.logsieves.models.LogSieveNode`
.. |LogSieveNodes| replace:: :class:`LogSieveNodes<sifter.logsifter.logsieves.models.LogSieveNode>`
.. |MailChute| replace:: :class:`~sifter.mailsifter.mailchutes.models.MailChute`
.. |MailChutes| replace:: :class:`MailChutes<sifter.mailsifter.mailchutes.models.MailChute>`
.. |MailCondenser| replace:: :class:`~sifter.mailsifter.mailcondensers.models.MailCondenser`
.. |MailCondensers| replace:: :class:`MailCondensers<sifter.mailsifter.mailcondensers.models.MailCondenser>`
.. |MailFitting| replace:: :class:`~MailFitting.mailsifter.mailcondensers.models.MailFitting`
.. |MailFittings| replace:: :class:`MailFittings<sifter.mailsifter.mailcondensers.models.MailFitting>`
.. |MailMunger| replace:: :class:`~sifter.mailsifter.mailmungers.models.MailMunger`
.. |MailMungers| replace:: :class:`MailMungers<sifter.mailsifter.mailmungers.models.MailMunger>`
.. |MailParser| replace:: :class:`~sifter.mailsifter.mailcondensers.models.MailParser`
.. |MailParsers| replace:: :class:`MailParsers<sifter.mailsifter.mailcondensers.models.MailParser>`
.. |MailRule| replace:: :class:`~sifter.mailsifter.mailsieves.models.MailRule`
.. |MailRules| replace:: :class:`MailRules<sifter.mailsifter.mailsieves.models.MailRule>`
.. |MailSieve| replace:: :class:`~sifter.mailsifter.mailsieves.models.MailSieve`
.. |MailSieves| replace:: :class:`MailSieves<sifter.mailsifter.mailsieves.models.MailSieve>`
.. |MailSieveNode| replace:: :class:`~sifter.mailsifter.mailsieves.models.MailSieveNode`
.. |MailSieveNodes| replace:: :class:`MailSieveNodes<sifter.mailsifter.mailsieves.models.MailSieveNode>`
.. |MongoDbEngine| replace:: :class:`~engines.mongodb.engine.MongoDbEngine`
.. |Monitor| replace:: :class:`~monitors.models.Monitor`
.. |Monitors| replace:: :class:`Monitors<monitors.models.Monitor>`
.. |Munger| replace:: :class:`~sifter.mungers.models.Munger`
.. |Mungers| replace:: :class:`Mungers<sifter.mungers.models.Munger>`
.. |Muzzle| replace:: :class:`~watchdogs.models.Muzzle`
.. |Muzzles| replace:: :class:`Muzzles<watchdogs.models.Muzzle>`
.. |OPERATOR_CHOICES| replace:: :const:`~cyphon.choices.OPERATOR_CHOICES`
.. |Passport| replace:: :class:`~ambassador.passports.models.Passport`
.. |Passports| replace:: :class:`Passports<ambassador.passports.models.Passport>`
.. |Pipe| replace:: :class:`~aggregator.pipes.models.Pipe`
.. |Pipes| replace:: :class:`Pipes<aggregator.pipes.models.Pipe>`
.. |PipeSpecSheet| replace:: :class:`~aggregator.pipes.models.PipeSpecSheet`
.. |PipeSpecSheets| replace:: :class:`PipeSpecSheets<aggregator.pipes.models.PipeSpecSheet>`
.. |Platform| replace:: :class:`~ambassador.platforms.models.Platform`
.. |Platforms| replace:: :class:`Platforms<ambassador.platforms.models.Platform>`
.. |Plumber| replace:: :class:`~aggregator.plumbers.models.Plumber`
.. |Plumbers| replace:: :class:`Plumbers<aggregator.plumbers.models.Plumber>`
.. |Procedure| replace:: :class:`~lab.procedures.models.Procedure`
.. |Procedures| replace:: :class:`Procedures<lab.procedures.models.Procedure>`
.. |Protocol| replace:: :class:`~lab.procedures.models.Protocol`
.. |Protocols| replace:: :class:`Protocols<lab.procedures.models.Protocol>`
.. |Pump| replace:: :class:`~aggregator.pumproom.pump.Pump`
.. |Pumps| replace:: :class:`Pumps<aggregator.pumproom.pump.Pump>`
.. |PumpRoom| replace:: :class:`~aggregator.pumproom.pumproom.PumpRoom`
.. |QueryFieldset| replace:: :class:`~cyphon.fieldsets.QueryFieldset`
.. |QueryFieldsets| replace:: :class:`QueryFieldsets<cyphon.fieldsets.QueryFieldset>`
.. |RealName| replace:: :class:`~codebooks.models.RealName`
.. |RealNames| replace:: :class:`RealNames<codebooks.models.RealName>`
.. |Record| replace:: :class:`~ambassador.records.models.Record`
.. |Records| replace:: :class:`Records<ambassador.records.models.Record>`
.. |Reservoir| replace:: :class:`~aggregator.reservoirs.models.Reservoir`
.. |Reservoirs| replace:: :class:`Reservoirs<aggregator.reservoirs.models.Reservoir>`
.. |ReservoirQuery| replace:: :class:`~query.reservoirqueries.reservoirquery.ReservoirQuery`
.. |ReservoirQueries| replace:: :class:`ReservoirQueries<query.reservoirqueries.reservoirquery.ReservoirQuery>`
.. |ReservoirQueryParameters| replace:: :class:`~query.reservoirqueries.models.ReservoirQueryParameters`
.. |Responder| replace:: :ref:`Responder<responder>`
.. |Rule| replace:: :class:`~sifter.sieves.models.Rule`
.. |Rules| replace:: :class:`Rules<sifter.sieves.models.Rule>`
.. |Parser| replace:: :class:`~rules.models.Parser`
.. |Parsers| replace:: :class:`~rules.models.Parsers`
.. |Sample| replace:: :class:`~aggregator.samples.models.Sample`
.. |Samples| replace:: :class:`Samples<aggregator.samples.models.Sample>`
.. |SEARCH_TASK_CHOICES| replace:: :const:`~cyphon.choices.SEARCH_TASK_CHOICES`
.. |SearchTerm| replace:: :class:`~target.searchterms.models.SearchTerm`
.. |SearchTerms| replace:: :class:`SearchTerms<target.searchterms.models.SearchTerm>`
.. |Sieve| replace:: :class:`~sifter.sieves.models.Sieve`
.. |Sieves| replace:: :class:`Sieves<sifter.sieves.models.Sieve>`
.. |SieveNode| replace:: :class:`~sifter.sieves.models.SieveNode`
.. |SieveNodes| replace:: :class:`SieveNodes<sifter.sieves.models.SieveNode>`
.. |Sorter| replace:: :class:`Sorter<engines.sorter.Sorter>`
.. |SortParams| replace:: :class:`SortParams<engines.sorter.SortParam>`
.. |Stamp| replace:: :class:`~ambassador.stamps.models.Stamp`
.. |Stamps| replace:: :class:`Stamps<ambassador.stamps.models.Stamp>`
.. |Stream| replace:: :class:`~aggregator.streams.models.Stream`
.. |Streams| replace:: :class:`Streams<aggregator.streams.models.Stream>`
.. |TARGET_TYPE_CHOICES| replace:: :const:`~cyphon.choices.TARGET_TYPE_CHOICES`
.. |Tag| replace:: :class:`~tags.models.Tag`
.. |Tags| replace:: :class:`Tags<tags.models.Tag>`
.. |TagRelation| replace:: :class:`~tags.models.TagRelation`
.. |TagRelations| replace:: :class:`Tags<tags.models.TagRelation>`
.. |Taste| replace:: :class:`~bottler.tastes.models.Taste`
.. |Tastes| replace:: :class:`Tastes<bottler.tastes.models.Taste>`
.. |Taxonomy| replace:: :class:`taxonomies.models.Taxonomy`
.. |Taxonomies| replace:: :class:`Taxonomies<taxonomies.models.Taxonomy>`
.. |Teaser| replace:: :class:`~teasers.models.Teaser>`
.. |Teasers| replace:: :class:`Teasers<teasers.models.Teaser>`
.. |TEXT_FIELDS| replace:: :const:`~cyphon.choices.TEXT_FIELDS`
.. |TIME_UNIT_CHOICES| replace:: :const:`~cyphon.choices.TIME_UNIT_CHOICES`
.. |TimeFrame| replace:: :class:`~target.timeframes.models.TimeFrame`
.. |TimeFrames| replace:: :class:`TimeFrames<target.timeframes.models.TimeFrame>`
.. |Topic| replace:: :class:`~tags.models.Topic`
.. |Topics| replace:: :class:`Tags<tags.models.Topic>`
.. |Transport| replace:: :class:`~ambassador.transport.Transport`
.. |Transports| replace:: :class:`Transports<ambassador.transport.Transport>`
.. |Trigger| replace:: :class:`~watchdogs.models.Trigger`
.. |Triggers| replace:: :class:`Triggers<watchdogs.models.Trigger>`
.. |Warehouse| replace:: :class:`~warehouses.models.Warehouse`
.. |Warehouses| replace:: :class:`Warehouses<watchdogs.models.Warehouse>`
.. |Watchdog| replace:: :class:`~watchdogs.models.Watchdog`
.. |Watchdogs| replace:: :class:`Watchdogs<watchdogs.models.Watchdog>`
.. |Visa| replace:: :class:`~ambassador.visas.models.Visa`
.. |Visas| replace:: :class:`Visas<ambassador.visas.models.Visa>`
"""

def setup(app):
    app.add_javascript('js/cyphon.js')
