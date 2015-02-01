from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from models import QuestionPlugin, RatingPlugin, RatingVote
from django.utils.translation import ugettext as _
from questions_and_ratings.models import QuestionVote


class CMSQuestionPlugin(CMSPluginBase):
    model = QuestionPlugin
    name = _("Question")
    render_template = "question.html"

    def render(self, context, instance, placeholder):
        current_user = context['request'].user
        if QuestionVote.objects.filter(user__pk=current_user.pk, answers__question=instance.question):
            context.update({
                "results": instance.question.get_results()
            })
        else:
            if "results" in context:
                del context["results"]
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
        current_user = context['request'].user
        if RatingVote.objects.filter(user__pk=current_user.pk, rating=instance.rating):
            context.update({
                "results": instance.rating.get_results()
            })
        else:
            if "results" in context:
                del context["results"]
        context.update({
            'rating': instance.rating,
            'object': instance,
            'placeholder': placeholder
        })
        return context


plugin_pool.register_plugin(CMSQuestionPlugin)
plugin_pool.register_plugin(CMSRatingPlugin)