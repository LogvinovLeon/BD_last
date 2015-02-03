from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class GenerateRaport(CMSApp):
    name = _("Generate Raport") # give your app a name, this is required
    urls = ["raports.urls"] # link your app to url configuration(s)

apphook_pool.register(GenerateRaport) # register your app