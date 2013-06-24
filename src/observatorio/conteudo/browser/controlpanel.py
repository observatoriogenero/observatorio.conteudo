# -*- coding: utf-8 -*-

from plone.app.registry.browser import controlpanel

from observatorio.conteudo.interfaces import IConteudoSettings

from z3c.form.browser.textlines import TextLinesFieldWidget


class ConteudoSettingsEditForm(controlpanel.RegistryEditForm):

    schema = IConteudoSettings
    label = u"Configuração dos vocabulários"
    description = u"Configuração dos vocabulários usados nos conteúdos do observatório"

    def updateFields(self):
        super(ConteudoSettingsEditForm, self).updateFields()
        self.fields['area_tematica'].widgetFactory = TextLinesFieldWidget
        self.fields['eixo_atuacao'].widgetFactory = TextLinesFieldWidget

    def updateWidgets(self):
        super(ConteudoSettingsEditForm, self).updateWidgets()


class ConteudoSettingsControlPanel(controlpanel.ControlPanelFormWrapper):
    form = ConteudoSettingsEditForm
