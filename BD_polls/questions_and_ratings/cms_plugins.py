from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from models import QuestionPlugin, RatingPlugin
from django.utils.translation import ugettext as _


class CMSQuestionPlugin(CMSPluginBase):
    model = QuestionPlugin
    name = _("Question")
    render_template = "question.html"

    def render(self, context, instance, placeholder):
        context.update({
            'question': instance.question,
            'object': instance,
            'placeholder': placeholder
        })
        return context


class CMSRatingPlugin(CMSPluginBase):
    model = RatingPlugin
    name = _("Rating")
    render_template = "rating.html"

    def render(self, context, instance, placeholder):
        context.update({
            'rating': instance.rating,
            'object': instance,
            'placeholder': placeholder
        })
        return context


plugin_pool.register_plugin(CMSQuestionPlugin)
plugin_pool.register_plugin(CMSRatingPlugin)