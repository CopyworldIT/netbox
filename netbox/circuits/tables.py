import django_tables2 as tables
from django_tables2.utils import Accessor

from tenancy.tables import COL_TENANT
from utilities.tables import BaseTable, TagColumn, ToggleColumn
from .models import Circuit, CircuitType, Provider

CIRCUITTYPE_ACTIONS = """
<a href="{% url 'circuits:circuittype_changelog' slug=record.slug %}" class="btn btn-default btn-xs" title="Change log">
    <i class="fa fa-history"></i>
</a>
{% if perms.circuit.change_circuittype %}
    <a href="{% url 'circuits:circuittype_edit' slug=record.slug %}?return_url={{ request.path }}"
      class="btn btn-xs btn-warning"><i class="glyphicon glyphicon-pencil" aria-hidden="true"></i></a>
{% endif %}
"""

STATUS_LABEL = """
<span class="label label-{{ record.get_status_class }}">{{ record.get_status_display }}</span>
"""


#
# Providers
#

class ProviderTable(BaseTable):
    pk = ToggleColumn()
    name = tables.LinkColumn()
    circuit_count = tables.Column(
        accessor=Accessor('count_circuits'),
        verbose_name='Circuits'
    )
    tags = TagColumn(
        url_name='circuits:provider_list'
    )

    class Meta(BaseTable.Meta):
        model = Provider
        fields = (
            'pk', 'name', 'asn', 'account', 'portal_url', 'noc_contact', 'admin_contact', 'circuit_count', 'tags',
        )
        default_columns = ('pk', 'name', 'asn', 'account', 'circuit_count')


#
# Circuit types
#

class CircuitTypeTable(BaseTable):
    pk = ToggleColumn()
    name = tables.LinkColumn()
    circuit_count = tables.Column(
        verbose_name='Circuits'
    )
    actions = tables.TemplateColumn(
        template_code=CIRCUITTYPE_ACTIONS,
        attrs={'td': {'class': 'text-right noprint'}},
        verbose_name=''
    )

    class Meta(BaseTable.Meta):
        model = CircuitType
        fields = ('pk', 'name', 'circuit_count', 'description', 'slug', 'actions')
        default_columns = ('pk', 'name', 'circuit_count', 'description', 'slug', 'actions')


#
# Circuits
#

class CircuitTable(BaseTable):
    pk = ToggleColumn()
    cid = tables.LinkColumn(
        verbose_name='ID'
    )
    provider = tables.LinkColumn(
        viewname='circuits:provider',
        args=[Accessor('provider.slug')]
    )
    status = tables.TemplateColumn(
        template_code=STATUS_LABEL
    )
    tenant = tables.TemplateColumn(
        template_code=COL_TENANT
    )
    a_side = tables.Column(
        verbose_name='A Side'
    )
    z_side = tables.Column(
        verbose_name='Z Side'
    )
    tags = TagColumn(
        url_name='circuits:circuit_list'
    )

    class Meta(BaseTable.Meta):
        model = Circuit
        fields = (
            'pk', 'cid', 'provider', 'type', 'status', 'tenant', 'a_side', 'z_side', 'install_date', 'commit_rate',
            'description', 'tags',
        )
        default_columns = ('pk', 'cid', 'provider', 'type', 'status', 'tenant', 'a_side', 'z_side', 'description')
