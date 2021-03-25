from Products.Archetypes.references import HoldingReference
from AccessControl import ClassSecurityInfo
from Products.Archetypes.public import *
from Products.CMFCore import permissions
from Products.CMFPlone.interfaces import IConstrainTypes
from Products.CMFCore.utils import getToolByName
from zope.interface import implements
from bika.lims.browser.widgets import DateTimeWidget

from bika.lims.content.bikaschema import BikaSchema
from baobab.lims import bikaMessageFactory as _
from baobab.lims import config
from baobab.lims.interfaces import IViralGenomicAnalysis
from bika.lims.browser.widgets import ReferenceWidget as bika_ReferenceWidget

from Products.DataGridField import CheckboxColumn
from Products.DataGridField import Column
from Products.DataGridField import DataGridField
from Products.DataGridField import DataGridWidget
from Products.DataGridField import LinesColumn
from Products.DataGridField import SelectColumn
from bika.lims.vocabularies import CatalogVocabulary


Project = ReferenceField(
    'Project',
    allowed_types=('Project',),
    relationship='ViralGenomicAnalysisProjects',
    referenceClass=HoldingReference,
    required=True,
    widget=bika_ReferenceWidget(
        label=_("Select Project"),
        size=30,
        showOn=True,
        description=_("Select the project for the viral genomic analysis."),
        visible={
         'edit': 'visible',
         'view': 'visible',
         'created': {'view': 'visible', 'edit': 'visible'},
         'extracted_genomic_material': {'view': 'invisible', 'edit': 'invisible'},
         'aliquoted': {'view': 'invisible', 'edit': 'invisible'},
         'genome_quantified': {'view': 'invisible', 'edit': 'invisible'},
         'viral_load_determined': {'view': 'invisible', 'edit': 'invisible'},
         'sequencing_library_preped': {'view': 'invisible', 'edit': 'invisible'},
     },
    )
)

DateCreated = DateTimeField(
    'DateCreated',
    mode="rw",
    read_permission=permissions.View,
    write_permission=permissions.ModifyPortalContent,
    widget=DateTimeWidget(
        label=_("Date Created"),
        description=_("Define when the Viral Genomic Analysis has been created."),
        show_time=True,
        visible={
         'edit': 'visible',
         'view': 'visible',
         'created': {'view': 'visible', 'edit': 'visible'},
         'extracted_genomic_material': {'view': 'invisible', 'edit': 'invisible'},
         'aliquoted': {'view': 'invisible', 'edit': 'invisible'},
         'genome_quantified': {'view': 'invisible', 'edit': 'invisible'},
         'viral_load_determined': {'view': 'invisible', 'edit': 'invisible'},
         'sequencing_library_preped': {'view': 'invisible', 'edit': 'invisible'},
     },
    )
)

WillExtract = BooleanField(
    'WillExtract',
    default=False,
    widget=BooleanWidget(
        label="Will Extract",
        description="Whether or not to Extract Genomic Material",
        visible={
         'edit': 'visible',
         'view': 'visible',
         'created': {'view': 'visible', 'edit': 'visible'},
         'extracted_genomic_material': {'view': 'invisible', 'edit': 'invisible'},
         'aliquoted': {'view': 'invisible', 'edit': 'invisible'},
         'genome_quantified': {'view': 'invisible', 'edit': 'invisible'},
         'viral_load_determined': {'view': 'invisible', 'edit': 'invisible'},
         'sequencing_library_preped': {'view': 'invisible', 'edit': 'invisible'},
     },
    )
)

WillAliquot = BooleanField(
    'WillAliquot',
    default=False,
    widget=BooleanWidget(
        label="Aliquoting",
        description="Whether new Aliquots will be created",
        visible={
         'edit': 'visible',
         'view': 'visible',
         'created': {'view': 'visible', 'edit': 'visible'},
         'extracted_genomic_material': {'view': 'invisible', 'edit': 'invisible'},
         'aliquoted': {'view': 'invisible', 'edit': 'invisible'},
         'genome_quantified': {'view': 'invisible', 'edit': 'invisible'},
         'viral_load_determined': {'view': 'invisible', 'edit': 'invisible'},
         'sequencing_library_preped': {'view': 'invisible', 'edit': 'invisible'},
     },
    )
)

WillQuantify = BooleanField(
    'WillQuantify',
    default=False,
    widget=BooleanWidget(
        label="Will Quantify",
        description="Whether Quantifying will occur",
        visible={
         'edit': 'visible',
         'view': 'visible',
         'created': {'view': 'visible', 'edit': 'visible'},
         'extracted_genomic_material': {'view': 'invisible', 'edit': 'invisible'},
         'aliquoted': {'view': 'invisible', 'edit': 'invisible'},
         'genome_quantified': {'view': 'invisible', 'edit': 'invisible'},
         'viral_load_determined': {'view': 'invisible', 'edit': 'invisible'},
         'sequencing_library_preped': {'view': 'invisible', 'edit': 'invisible'},
     },
    )
)

WillViralLoadDetermine = BooleanField(
    'WillViralLoadDetermine',
    default=False,
    widget=BooleanWidget(
        label="Confirm Viral Load Determine",
        description="Whether viral load will be determined",
        visible={
         'edit': 'visible',
         'view': 'visible',
         'created': {'view': 'visible', 'edit': 'visible'},
         'extracted_genomic_material': {'view': 'invisible', 'edit': 'invisible'},
         'aliquoted': {'view': 'invisible', 'edit': 'invisible'},
         'genome_quantified': {'view': 'invisible', 'edit': 'invisible'},
         'viral_load_determined': {'view': 'invisible', 'edit': 'invisible'},
         'sequencing_library_preped': {'view': 'invisible', 'edit': 'invisible'},
     },
    )
)

WillLibraryPrep = BooleanField(
    'WillLibraryPrep',
    default=False,
    widget=BooleanWidget(
        label="Confirm Sequence Library Prep",
        description="Confirm if there will be Sequence Library Prep",
        visible={
         'edit': 'visible',
         'view': 'visible',
         'created': {'view': 'visible', 'edit': 'visible'},
         'extracted_genomic_material': {'view': 'invisible', 'edit': 'invisible'},
         'aliquoted': {'view': 'invisible', 'edit': 'invisible'},
         'genome_quantified': {'view': 'invisible', 'edit': 'invisible'},
         'viral_load_determined': {'view': 'invisible', 'edit': 'invisible'},
         'sequencing_library_preped': {'view': 'invisible', 'edit': 'invisible'},
     },
    )
)

ExtractGenomicMaterial = DataGridField(
    'ExtractGenomicMaterial',
    schemata='Extract Genomic Material',
    validators=('extractgenomicmaterialvalidator'),
    allow_insert=True,
    allow_delete=True,
    allow_reorder=False,
    allow_empty_rows=False,
    allow_oddeven=True,
    columns=('VirusSample',
             'Method',
             'ExtractionBarcode',
             'Volume',
             'Unit',
             'HeatInactivated',
             'WasKitUsed',
             'KitNumber',
             'Notes',
             ),
    widget=DataGridWidget(
        label=_('Extract Genomic Materials'),
        columns={
            'VirusSample': SelectColumn(
                'Virus Sample', 
                vocabulary='Vocabulary_VirusSample_by_ProjectUID',
                visible={
                 'edit': 'visible',
                 'view': 'visible',
                 'created': {'view': 'visible', 'edit': 'visible'},
                 'extracted_genomic_material': {'view': 'visible', 'edit': 'visible'},
                 'aliquoted': {'view': 'invisible', 'edit': 'invisible'},
                 'genome_quantified': {'view': 'invisible', 'edit': 'invisible'},
                 'viral_load_determined': {'view': 'invisible', 'edit': 'invisible'},
                 'sequencing_library_preped': {'view': 'invisible', 'edit': 'invisible'},
             },
                ),
            'Method': SelectColumn('Method', 
                vocabulary='Vocabulary_Method',
                visible={
                 'edit': 'visible',
                 'view': 'visible',
                 'created': {'view': 'visible', 'edit': 'visible'},
                 'extracted_genomic_material': {'view': 'visible', 'edit': 'visible'},
                 'aliquoted': {'view': 'invisible', 'edit': 'invisible'},
                 'genome_quantified': {'view': 'invisible', 'edit': 'invisible'},
                 'viral_load_determined': {'view': 'invisible', 'edit': 'invisible'},
                 'sequencing_library_preped': {'view': 'invisible', 'edit': 'invisible'},
             },
                ),
            'ExtractionBarcode': Column('Extraction Barcode',
                visible={
                 'edit': 'visible',
                 'view': 'visible',
                 'created': {'view': 'visible', 'edit': 'visible'},
                 'extracted_genomic_material': {'view': 'visible', 'edit': 'visible'},
                 'aliquoted': {'view': 'invisible', 'edit': 'invisible'},
                 'genome_quantified': {'view': 'invisible', 'edit': 'invisible'},
                 'viral_load_determined': {'view': 'invisible', 'edit': 'invisible'},
                 'sequencing_library_preped': {'view': 'invisible', 'edit': 'invisible'},
             },
                ),
            'Volume': Column('Volume',
                visible={
                 'edit': 'visible',
                 'view': 'visible',
                 'created': {'view': 'visible', 'edit': 'visible'},
                 'extracted_genomic_material': {'view': 'visible', 'edit': 'visible'},
                 'aliquoted': {'view': 'invisible', 'edit': 'invisible'},
                 'genome_quantified': {'view': 'invisible', 'edit': 'invisible'},
                 'viral_load_determined': {'view': 'invisible', 'edit': 'invisible'},
                 'sequencing_library_preped': {'view': 'invisible', 'edit': 'invisible'},
             },
                ),
            'Unit': Column('Unit',
                visible={
                 'edit': 'visible',
                 'view': 'visible',
                 'created': {'view': 'visible', 'edit': 'visible'},
                 'extracted_genomic_material': {'view': 'visible', 'edit': 'visible'},
                 'aliquoted': {'view': 'invisible', 'edit': 'invisible'},
                 'genome_quantified': {'view': 'invisible', 'edit': 'invisible'},
                 'viral_load_determined': {'view': 'invisible', 'edit': 'invisible'},
                 'sequencing_library_preped': {'view': 'invisible', 'edit': 'invisible'},
             },
                    ),
            'HeatInactivated': CheckboxColumn('Heat Inactivated',
                visible={
                 'edit': 'visible',
                 'view': 'visible',
                 'created': {'view': 'visible', 'edit': 'visible'},
                 'extracted_genomic_material': {'view': 'visible', 'edit': 'visible'},
                 'aliquoted': {'view': 'invisible', 'edit': 'invisible'},
                 'genome_quantified': {'view': 'invisible', 'edit': 'invisible'},
                 'viral_load_determined': {'view': 'invisible', 'edit': 'invisible'},
                 'sequencing_library_preped': {'view': 'invisible', 'edit': 'invisible'},
             },
                    ),
            'WasKitUsed': CheckboxColumn('Was Kit Used',
                visible={
                 'edit': 'visible',
                 'view': 'visible',
                 'created': {'view': 'visible', 'edit': 'visible'},
                 'extracted_genomic_material': {'view': 'visible', 'edit': 'visible'},
                 'aliquoted': {'view': 'invisible', 'edit': 'invisible'},
                 'genome_quantified': {'view': 'invisible', 'edit': 'invisible'},
                 'viral_load_determined': {'view': 'invisible', 'edit': 'invisible'},
                 'sequencing_library_preped': {'view': 'invisible', 'edit': 'invisible'},
             },
                    ),
            'KitNumber': Column('Kit Lot #',
                visible={
                 'edit': 'visible',
                 'view': 'visible',
                 'created': {'view': 'visible', 'edit': 'visible'},
                 'extracted_genomic_material': {'view': 'visible', 'edit': 'visible'},
                 'aliquoted': {'view': 'invisible', 'edit': 'invisible'},
                 'genome_quantified': {'view': 'invisible', 'edit': 'invisible'},
                 'viral_load_determined': {'view': 'invisible', 'edit': 'invisible'},
                 'sequencing_library_preped': {'view': 'invisible', 'edit': 'invisible'},
             },
                    ),
            'Notes': LinesColumn('Notes',
                visible={
                 'edit': 'visible',
                 'view': 'visible',
                 'created': {'view': 'visible', 'edit': 'visible'},
                 'extracted_genomic_material': {'view': 'visible', 'edit': 'visible'},
                 'aliquoted': {'view': 'invisible', 'edit': 'invisible'},
                 'genome_quantified': {'view': 'invisible', 'edit': 'invisible'},
                 'viral_load_determined': {'view': 'invisible', 'edit': 'invisible'},
                 'sequencing_library_preped': {'view': 'invisible', 'edit': 'invisible'},
             },
                    ),
        },
    )
)

GenomeQuantification = DataGridField(
    'GenomeQuantification',
    schemata='Genome Quantification',
    allow_insert=True,
    allow_delete=True,
    allow_reorder=False,
    allow_empty_rows=False,
    allow_oddeven=True,
    columns=('VirusSampleRNAorDNA',
             'FluorimeterConc',
             'NanometerQuantity',
             'NanometerRatio',
             ),
    widget=DataGridWidget(
        label=_('Fluorimeter/Nanometer'),
        columns={
            'VirusSampleRNAorDNA': SelectColumn(
                'Virus Sample by RNA/DNA',
                # vocabulary='Vocabulary_Sample_RNA_or_DNA',
                vocabulary='Vocabulary_VLD_Sample_RNA_or_DNA',
                visible={
                 'edit': 'visible',
                 'view': 'visible',
                 'created': {'view': 'visible', 'edit': 'visible'},
             },
                ),
            'FluorimeterConc': Column('Fluorimeter Conc (ng/ul)',
                visible={
                 'edit': 'visible',
                 'view': 'visible',
                 'created': {'view': 'visible', 'edit': 'visible'},
             },
                ),
            'NanometerQuantity': Column('Nanometer Conc (ng/ul)',
                visible={
                 'edit': 'visible',
                 'view': 'visible',
                 'created': {'view': 'visible', 'edit': 'visible'},
             },
                ),
            'NanometerRatio': Column('Nanometer Ratio (260/280)',
                visible={
                 'edit': 'visible',
                 'view': 'visible',
                 'created': {'view': 'visible', 'edit': 'visible'},
             },
                )
        }
    )
)

VirusAliquot = ReferenceField(
    'VirusAliquot',
    schemata='Virus Sample Aliquot',
    multiValued=1,
    allowed_types=('VirusAliquot',),
    relationship='ViralGenomicAnalysisVirusAliquot',
    referenceClass=HoldingReference,
    mode="rw",
    read_permission=permissions.View,
    write_permission=permissions.ModifyPortalContent,
    widget=bika_ReferenceWidget(
        label=_("Select Virus Aliquot"),
        visible={
         'edit': 'visible',
         'view': 'visible',
         'created': {'view': 'visible', 'edit': 'visible'},
     },
        size=30,
        showOn=True,
        description=_("Select the Virus Aliquot for the viral genomic analysis."),
    )
)

ViralLoadDeterminationTitle = StringField(
    'ViralLoadDeterminationTitle',
    schemata='Viral Load Determination',
    widget=StringWidget(
        label=_("Title"),
        size=30,
    )
)

ViralLoadDeterminationDescription = TextField(
    'ViralLoadDeterminationDescription',
    schemata='Viral Load Determination',
    widget=TextAreaWidget(
        label=_("Description"),
    )
)

ViralLoadDeterminationGeneName = StringField(
    'ViralLoadDeterminationGeneName',
    schemata='Viral Load Determination',
    widget=StringWidget(
        label=_("Gene name"),
    )
)
ViralLoadDeterminationDate = DateTimeField(
    'ViralLoadDeterminationDate',
    schemata='Viral Load Determination',
    mode="rw",
    read_permission=permissions.View,
    write_permission=permissions.ModifyPortalContent,
    widget=DateTimeWidget(
        label=_("Date"),
        description=_("Viral Load Determination date."),
        show_time=False,
    )
)

ViralLoadDetermination = DataGridField(
    'ViralLoadDetermination',
    schemata='Viral Load Determination',
    allow_insert=True,
    allow_delete=True,
    allow_reorder=False,
    allow_empty_rows=False,
    allow_oddeven=True,
    columns=('VirusSampleRNAorDNA',
             'ctValue',
             'KitNumber',
             'Result',
             'Verification',
             'AddToReport',
             'Notes',
             ),
    widget=DataGridWidget(
        label=_('Viral Load Determination(RT-PCR)'),
        columns={
            'VirusSampleRNAorDNA': SelectColumn(
                'Virus Sample by RNA/DNA',
                # vocabulary='Vocabulary_Sample_RNA_or_DNA'),
                vocabulary='Vocabulary_VLD_Sample_RNA_or_DNA'),
            'ctValue': Column('ct Value'),
            'KitNumber': Column('Kit Lot #'),
            'Result': SelectColumn(
                'Result',
                vocabulary='Vocabulary_VLD_Result'),
            'Verification': SelectColumn(
                'Verification',
                vocabulary='Vocabulary_VLD_Verification'),
            'AddToReport': CheckboxColumn('Add to report'),
            'Notes': LinesColumn('Notes')
        }
    )
)
SequencingLibraryPrep = DataGridField(
    'SequencingLibraryPrep',
    schemata='Sequencing Library Prep',
    allow_insert=True,
    allow_delete=True,
    allow_reorder=False,
    allow_empty_rows=False,
    allow_oddeven=True,
    columns=('VirusSampleRNAorDNA',
             'Method',
             'LibraryID',
             'Notes',
             ),
    widget=DataGridWidget(
        label=_('Sequencing Library Prep'),
        columns={
            'VirusSampleRNAorDNA': SelectColumn(
                'Virus Sample by RNA/DNA',
                vocabulary='Vocabulary_VLD_Sample_RNA_or_DNA',
                ),
            'Method': SelectColumn('Method', vocabulary='Vocabulary_Method'),
            'LibraryID': Column('Library ID'),
            'Notes': LinesColumn('Notes'),
        }
    )
)
schema = BikaSchema.copy() + Schema((
    Project,
    DateCreated,
    WillExtract,
    WillAliquot,
    WillQuantify,
    WillViralLoadDetermine,
    WillLibraryPrep,
    ExtractGenomicMaterial,
    VirusAliquot,
    GenomeQuantification,
    ViralLoadDeterminationTitle,
    ViralLoadDeterminationDescription,
    ViralLoadDeterminationGeneName,
    ViralLoadDeterminationDate,
    ViralLoadDetermination,
    SequencingLibraryPrep,
))

schema['title'].widget.visible = {'view': 'visible', 'edit': 'visible'}
schema['description'].widget.visible = {'view': 'visible', 'edit': 'visible'}

class ViralGenomicAnalysis(BaseContent):
    security = ClassSecurityInfo()
    implements(IViralGenomicAnalysis, IConstrainTypes)
    displayContentsTab = False
    schema = schema
    _at_rename_after_creation = True

    def _renameAfterCreation(self, check_auto_id=False):
        from bika.lims.idserver import renameAfterCreation
        renameAfterCreation(self)

    def getProjectUID(self):
        return self.getProject().UID() if self.getProject() else None

    # def prepare_extract_genomic_material(self):
    #
    #     extract_genomic_material_rows = self.getExtractGenomicMaterial()
    #     prepared_extracts = []
    #
    #     for extract in extract_genomic_material_rows:
    #         prepared_extract = {
    #             'title': extract.Title(),
    #             'virus_sample': self.get_virus_sample(extract),
    #             'heat_inactivated': extract.getField('HeatInactivated').get(extract),
    #             'method': self.get_method(extract),
    #             'extraction_barcode': extract.getField('ExtractionBarcode').get(extract),
    #             'volume': extract.getField('Volume').get(extract),
    #             'unit': extract.getField('Unit').get(extract),
    #             'was_kit_used': extract.getField('WasKitUsed').get(extract),
    #             'kit_number': extract.getField('KitNumber').get(extract),
    #             'notes': extract.getField('Notes').get(extract),
    #         }
    #         prepared_extracts.append(prepared_extract)
    #
    #     return prepared_extracts

    def prepare_virus_aliquots(self):
        virus_aliquots = self.getVirusAliquot()
        virus_aliquots_dict = {}

        for virus_aliquot in virus_aliquots:
            parent_sample = self.get_parent_sample(virus_aliquot)
            prepared_aliquot_list = self.get_prepared_aliquots(virus_aliquot.getAliquotSample())
            virus_aliquots_dict[parent_sample] = prepared_aliquot_list

        print(virus_aliquots_dict)
        return virus_aliquots_dict

    def get_prepared_aliquots(self, aliquot_rows):
        prepared_aliquots = []

        for aliquot in aliquot_rows:
            prepared_extract = {
                "barcode": aliquot.getField('Barcode').get(aliquot),
                "volume": aliquot.getField('Volume').get(aliquot),
                "unit": aliquot.getField('Unit').get(aliquot),
                "sample_type": self.get_sample_type(aliquot),
                'date_created': aliquot.getField('DateCreated').get(aliquot).strftime("%Y-%m-%d %H:%M"),
                # 'time_created': aliquot.getField('DateCreated').get(aliquot).strftime("%H:%M:%S"),
                # 'date_created': aliquot.getField('DateCreated').get(aliquot),
            }
            prepared_aliquots.append(prepared_extract)

        return prepared_aliquots

    def get_virus_sample(self, extract):
        try:
            virus_sample = extract.getField('VirusSample').get(extract)
            return virus_sample.Title()
        except:
            return ''

    def get_parent_sample(self, virus_aliquot):
        try:
            parent_sample = virus_aliquot.getField('ParentSample').get(virus_aliquot)
            return parent_sample.Title()
        except:
            return ''

    def get_sample_type(self, aliquot):
        try:
            sample_type = aliquot.getField('SampleType').get(aliquot)
            return sample_type.Title()
        except:
            return ''

    def get_method(self, extract):
        try:
            method = extract.getField('Method').get(extract)
            return method.Title()
        except:
            return ''

    def Vocabulary_PassFail(self):
        return DisplayList([('Pass', 'Pass'),('Fail', 'Fail')])

    def Vocabulary_Sample(self):
        vocabulary = CatalogVocabulary(self)
        vocabulary.catalog = 'bika_catalog'
        return vocabulary(allow_blank=True, portal_type='VirusSample')

    def getVirusSamplesByProjectUID(self, project_uid=None):
        # TODO: which catalog?
        pc = getToolByName(self, 'portal_catalog')
        # TODO: Add getProjectUID index or column instead,
        # so that self.getProjectUID will be available
        items = [('','')]
        if not project_uid:
            project_uid = self.getProjectUID()
        if not project_uid:
            return items

        brains = pc(portal_type="VirusSample", getProjectUID=project_uid)
        if not brains:
            return items
        return [('', '')] + [(c.UID, c.Title) for c in brains]

    def Vocabulary_VirusSample_by_ProjectUID(self, project_uid=None):
        return DisplayList(self.getVirusSamplesByProjectUID())

    def Vocabulary_Sample_RNA_or_DNA(self):
        pc = getToolByName(self, 'bika_catalog')
        # TODO: Add getProjectUID index or column instead,
        # so that self.getProjectUID will be available
        project_uid = self.getProjectUID()
        if not project_uid:
            items = [('','')]
            return DisplayList(items)

        # TODO:
        # filter by prefix or title
        # add prefix/title index or column
        brains = pc(portal_type="VirusSample", getProjectUID=project_uid)
        if not brains:
            brians = []
        items = [('', '')] + [(c.UID, c.Title) for c in brains]
        return DisplayList(items)

    def Vocabulary_VLD_Sample_RNA_or_DNA(self):
        pc = getToolByName(self, 'portal_catalog')

        # TODO: Add getProjectUID index or column instead,
        project_uid = self.getProjectUID()
        if not project_uid:
            items = [('','')]
            return DisplayList(items)

        rna_dna_sample_types = self.getRNAorDNASampleTypes()
        items = [('', '')]
        brains = pc(portal_type="Sample", getProjectUID=project_uid)
        for brain in brains:
            obj = brain.getObject()
            if obj.getField('SampleType').get(obj) in rna_dna_sample_types:
                items.append((obj.UID(), obj.Title()))

        return DisplayList(items)

    def getRNAorDNASampleTypes(self):
        bsc = getToolByName(self, 'bika_setup_catalog')
        brains = bsc(portal_type='SampleType', inactive_state='active')
        dna_rna_sample_types = []

        for brain in brains:
            obj = brain.getObject()
            if obj.getField('Prefix').get(obj).lower() in ('rna', 'dna'):
                dna_rna_sample_types.append(obj)

        return dna_rna_sample_types

    def Vocabulary_Method(self):
        vocabulary = CatalogVocabulary(self)
        vocabulary.catalog = 'portal_catalog'
        pc = getToolByName(self, 'portal_catalog')
        brains = pc(portal_type="Method")
        items = [('', '')] + [(c.UID, c.Title) for c in brains]
        return DisplayList(items)

    def Vocabulary_VLD_Result(self):
        return DisplayList([('', ''), ('Positive', 'Positive'), ('Negative', 'Negative'), ('Not determined', 'Not determined')])

    def Vocabulary_VLD_Verification(self):
        return DisplayList([('', ''), ('Verified', 'Verified'), ('Retracted', 'Retracted')])

registerType(ViralGenomicAnalysis, config.PROJECTNAME)
