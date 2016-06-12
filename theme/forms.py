from django import forms
from django.contrib.auth.models import User
from django.core.files.images import get_image_dimensions
from multiselectfield import MultiSelectField
from models import StudentProfile, CompanyProfile, StudentSearchFormModel, SponsorshipPackage
from models import DAY_CHOICES, GRADE_LEVEL_CHOICES, MAJOR_CHOICES, VOLUNTEER_CHOICES
from django.forms.formsets import BaseFormSet

class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Email  (required)'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password  (required)'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password  (again)'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First name  (required)'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last name  (required)'}))

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name')

    def clean_password2(self):
        password = self.cleaned_data.get("password", "")
        password2 = self.cleaned_data["password2"]
        if password != password2:
            raise forms.ValidationError("The two password fields didn't match.")
        return password2


class StudentProfileForm(forms.ModelForm):
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Phone number"}),  required=False)
    hometown = forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Hometown"}), required=False)
    state = forms.CharField(widget=forms.TextInput(attrs={'placeholder':"State", 'maxlength':2}), required=False)
    bio = forms.CharField(widget=forms.Textarea(attrs={'placeholder': '''Bio  (a quick blurb about your work history, your talents, accomplishments etc.)'''}), required=False)
    major = forms.MultipleChoiceField(widget=forms.SelectMultiple(), choices=MAJOR_CHOICES)
    minor = forms.MultipleChoiceField(widget=forms.SelectMultiple(), choices=MAJOR_CHOICES, required=False)
    grade_level = forms.MultipleChoiceField(widget=forms.SelectMultiple(), choices=GRADE_LEVEL_CHOICES)
    website = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "linkedin, portfolio, personal site, etc"}), required=False)
    GPA = forms.DecimalField(widget=forms.TextInput(), required=False)

    class Meta:
        model = StudentProfile
        fields = ('phone_number', 'hometown', 'state', 'open_to_relocation', 'bio', 'picture', 'resume', 'grade_level', 'major', 'minor', 'website', 'GPA')

    def clean_resume(self):
        resume = self.cleaned_data['resume']

        try:
            #validate content type
            main, sub = resume.content_type.split('/')
            if not (sub in ['pdf']):
                raise forms.ValidationError(u'Please use a PDF')

            resume = self.cleaned_data.get('image',False)
            if resume:
                if resume._size > 8*1024*1024:
                    raise ValidationError("Resume file too large ( > 8mb )")
                return resume

        except AttributeError:
            pass

        except TypeError:
            pass

        return resume

    def clean_picture(self):
        picture = self.cleaned_data['picture']

        try:
            w, h = get_image_dimensions(picture)

            #validate dimensions
            max_width = max_height = 4000
            if w > max_width or h > max_height:
                raise forms.ValidationError(
                    u'Please use an image that is '
                    '%s x %s pixels or smaller.' % (max_width, max_height))

            #validate content type
            main, sub = picture.content_type.split('/')
            if not (main == 'image' and sub in ['jpeg', 'pjpeg', 'gif', 'png']):
                raise forms.ValidationError(u'Please use a JPEG, '
                    'GIF or PNG image.')

            #validate file size
            image = self.cleaned_data.get('image',False)
            if image:
                if image._size > 1*1024*1024:
                    raise ValidationError("Image file too large ( > 1mb )")
                return image

        except AttributeError:
            pass

        except TypeError:
            return picture

        return picture



class CompanyProfileForm(forms.ModelForm):
    company = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Company name (required)'}))
    mood = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'How are you feeling today?'}), required=False)
    company_bio = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'A short blurb about who your company is and what you do.'}), required=False)
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Phone number'}), required=False)
    public_email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Public email '}), required=False)
    company_website = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Application website'}), required=False)
    majors_wanted = forms.MultipleChoiceField(widget=forms.SelectMultiple(), choices=MAJOR_CHOICES)
    days_attending = forms.MultipleChoiceField(widget=forms.SelectMultiple() , choices=DAY_CHOICES)
    grade_level_wanted = forms.MultipleChoiceField(widget=forms.SelectMultiple(), choices=GRADE_LEVEL_CHOICES)
    number_of_tables = forms.IntegerField()
    sponsor = forms.ChoiceField(choices=[(s.title,s.title) for s in SponsorshipPackage.objects.all()], widget=forms.RadioSelect, required=False)
    interview_friday_from = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "12:00pm"}),required=False)
    interview_friday_to = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "1:00pm"}), required=False)
    interview_saturday_from = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "12:00pm"}),required=False)
    interview_saturday_to = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "1:00pm"}), required=False)

    class Meta:
        model = CompanyProfile
        fields = ('company', 'public_email', 'phone_number', 'company_website' , 'logo' , 
            'days_attending', 'majors_wanted', 'grade_level_wanted', 'company_bio',
            "mood", 'number_of_tables', 'sponsor', 'interview_rooms_friday', 
            'interview_friday_from', 'interview_friday_to', 'interview_rooms_saturday',
            'interview_saturday_from' , 'interview_saturday_to')

    def clean_picture(self):
        picture = self.cleaned_data['picture']

        try:
            w, h = get_image_dimensions(picture)

            #validate dimensions
            max_width = max_height = 2400
            if w > max_width or h > max_height:
                raise forms.ValidationError(
                    u'Please use an image that is '
                    '%s x %s pixels or smaller.' % (max_width, max_height))

            #validate content type
            main, sub = picture.content_type.split('/')
            if not (main == 'image' and sub in ['jpeg', 'pjpeg', 'gif', 'png']):
                raise forms.ValidationError(u'Please use a JPEG, '
                    'GIF or PNG image.')

            #validate file size
            image = self.cleaned_data.get('image',False)
            if image:
                if image._size > 4*1024*1024:
                    raise forms.ValidationError("Image file too large ( > 4mb )")
                return image

        except AttributeError:
            pass

        except TypeError:
            return picture


        return picture

class RepForm(forms.Form):
    """
    Form for individual representative signups
    """
    rep = forms.CharField(
                    max_length=100,
                    widget=forms.TextInput(attrs={
                        'placeholder': 'Representative\'s name',
                    }),
                    required=False)
    is_alumni = forms.BooleanField(required=False)

class BaseRepFormSet(BaseFormSet):
    def clean(self):
        """
        Adds validation to check that no two links have the same anchor or URL
        and that all links have both an anchor and URL.
        """
        if any(self.errors):
            return

        reps = []
        duplicates = False

        for form in self.forms:
            if form.cleaned_data:
                rep = form.cleaned_data['rep']

                # Check that no two links have the same anchor or URL
                if rep:
                    if rep in reps:
                        duplicates = True
                    reps.append(rep)

                if duplicates:
                    raise forms.ValidationError(
                        'Links must have unique anchors and URLs.',
                        code='duplicate_links'
                    )


class EditCompanyProfileForm(forms.ModelForm):
    company = forms.CharField(widget=forms.TextInput())
    majors_wanted = forms.MultipleChoiceField(widget=forms.SelectMultiple(), choices=MAJOR_CHOICES)
    days_attending = forms.MultipleChoiceField(widget=forms.SelectMultiple() , choices=DAY_CHOICES)
    grade_level_wanted = forms.MultipleChoiceField(widget=forms.SelectMultiple(), choices=GRADE_LEVEL_CHOICES)
    number_of_tables = forms.IntegerField()
    sponsor = forms.ChoiceField(choices=[(s.title,s.title) for s in SponsorshipPackage.objects.all()], widget=forms.RadioSelect)
    class Meta:
        model = CompanyProfile
        fields = ('company', 'phone_number', 'company_website' , 'logo' , 
            'days_attending', 'majors_wanted', 'grade_level_wanted', 'company_bio', 'number_of_tables', 
            'sponsor', 'interview_rooms_friday', 
            'interview_friday_from', 'interview_friday_to', 'interview_rooms_saturday',
            'interview_saturday_from' , 'interview_saturday_to')

class CompanySearchForm(forms.ModelForm):
    majors_wanted = forms.ChoiceField(widget=forms.SelectMultiple(), choices=MAJOR_CHOICES)
    class Meta:
        model = CompanyProfile
        fields = ('company', 'days_attending', 'majors_wanted', 'grade_level_wanted')

class StudentSearchForm(forms.ModelForm):
    major_wanted = forms.ChoiceField(widget=forms.SelectMultiple(), choices=MAJOR_CHOICES)
    minimum_GPA = forms.DecimalField(widget=forms.TextInput(attrs = {'maxlength': 4, 'placeholder': "Minimum GPA" }))
    class Meta:
        model = StudentSearchFormModel
        fields = ('name','open_to_relocation', 'major_wanted', 'grade_level_wanted', 'minimum_GPA')

    def clean_minimum_GPA(self):
        minimum_GPA = self.cleaned_data['minimum_GPA']
        try:
            if not minimum_GPA.isdigit():
                raise forms.ValidationError("Enter a demical")
            if minimum_GPA < 0 or minimum_GPA > 4:
                raise forms.ValidationError("Enter a decimal between 0.00 and 4.00")

        except AttributeError:
            pass

        return minimum_GPA


from django.forms.extras import SelectDateWidget
from django.core.urlresolvers import reverse
from django.utils.translation import ungettext, ugettext_lazy as _

FILTER_CHOICE_CONTAINS = "1"
FILTER_CHOICE_DOESNT_CONTAIN = "2"

# Exact matches
FILTER_CHOICE_EQUALS = "3"
FILTER_CHOICE_DOESNT_EQUAL = "4"

FILTER_CHOICE_BETWEEN = "5"

# Multiple values
FILTER_CHOICE_CONTAINS_ANY = "6"
FILTER_CHOICE_CONTAINS_ALL = "7"
FILTER_CHOICE_DOESNT_CONTAIN_ANY = "8"
FILTER_CHOICE_DOESNT_CONTAIN_ALL = "9"

TEXT_FILTER_CHOICES = (
    ("", _("Nothing")),
    (FILTER_CHOICE_CONTAINS, _("Contains")),
    (FILTER_CHOICE_DOESNT_CONTAIN, _("Doesn't contain")),
    (FILTER_CHOICE_EQUALS, _("Equals")),
    (FILTER_CHOICE_DOESNT_EQUAL, _("Doesn't equal")),
)

DATE_FILTER_CHOICES = (
    ("", _("Nothing")),
    (FILTER_CHOICE_BETWEEN, _("Is between")),
)

CHOICE_FILTER_CHOICES = (
    ("", _("Nothing")),
    (FILTER_CHOICE_CONTAINS_ANY, _("Equals any")),
    (FILTER_CHOICE_DOESNT_CONTAIN_ANY, _("Doesn't equal any")),
)

MULTIPLE_FILTER_CHOICES = (
    ("", _("Nothing")),
    (FILTER_CHOICE_CONTAINS_ANY, _("Contains any")),
    (FILTER_CHOICE_CONTAINS_ALL, _("Contains all")),
    (FILTER_CHOICE_DOESNT_CONTAIN_ANY, _("Doesn't contain any")),
    (FILTER_CHOICE_DOESNT_CONTAIN_ALL, _("Doesn't contain all")),
)

date_filter_field = forms.ChoiceField(label=" ", required=False,
                                      choices=DATE_FILTER_CHOICES)

choice_filter_field = forms.ChoiceField(label=" ", required=False,
                                        choices=CHOICE_FILTER_CHOICES)

text_filter_field = forms.ChoiceField(label=" ", required=False,
                                      choices=TEXT_FILTER_CHOICES)

multiple_filter_field = forms.ChoiceField(label=" ", required=False,
                                          choices=MULTIPLE_FILTER_CHOICES)



FILTER_FUNCS = {
    FILTER_CHOICE_CONTAINS:
        lambda val, field: val.lower() in field.lower(),
    FILTER_CHOICE_DOESNT_CONTAIN:
        lambda val, field: val.lower() not in field.lower(),
    FILTER_CHOICE_EQUALS:
        lambda val, field: val.lower() == field.lower(),
    FILTER_CHOICE_DOESNT_EQUAL:
        lambda val, field: val.lower() != field.lower(),
    FILTER_CHOICE_BETWEEN:
        lambda val_from, val_to, field: (
            (not val_from or val_from <= field) and
            (not val_to or val_to >= field)
        ),
    FILTER_CHOICE_CONTAINS_ANY:
        lambda val, field: set(val) & set(split_choices(field)),
    FILTER_CHOICE_CONTAINS_ALL:
        lambda val, field: set(val) == set(split_choices(field)),
    FILTER_CHOICE_DOESNT_CONTAIN_ANY:
        lambda val, field: not set(val) & set(split_choices(field)),
    FILTER_CHOICE_DOESNT_CONTAIN_ALL:
        lambda val, field: set(val) != set(split_choices(field)),
}

MULTIPLE = ("GradeLevelWanted", "MajorsWanted", "DaysAttending")
CHOICES = ("HasSubmittedPayment")
DATES = ()

class EntriesForm(forms.Form):
    """
    Form with a set of fields dynamically assigned that can be used to
    filter entries for the given ``forms.models.Form`` instance.
    """

    def __init__(self, form, request, *args, **kwargs):
        """
        Iterate through the fields of the ``forms.models.Form`` instance and
        create the form fields required to control including the field in
        the export (with a checkbox) or filtering the field which differs
        across field types. User a list of checkboxes when a fixed set of
        choices can be chosen from, a pair of date fields for date ranges,
        and for all other types provide a textbox for text search.
        """
        self.form = form
        self.request = request
        self.form_fields = sorted(list(CompanyProfile._meta.get_all_field_names()))
        super(EntriesForm, self).__init__(*args, **kwargs)
        for field in self.form_fields:
            field_key = "field_" + field
            # Checkbox for including in export.
            self.fields["%s_export" % field_key] = forms.BooleanField(
                label=field, initial=True, required=False)
            if field.strip("_") in CHOICES:
                # A fixed set of choices to filter by.
                choices = ((True, _("True")), (False, _("False")))
                contains_field = forms.MultipleChoiceField(label=" ",
                    choices=choices, widget=forms.CheckboxSelectMultiple(),
                    required=False)
                self.fields["%s_filter" % field_key] = choice_filter_field
                self.fields["%s_contains" % field_key] = contains_field
            elif field.strip("_") in MULTIPLE:
                # A fixed set of choices to filter by, with multiple
                # possible values in the entry field.
                if field.strip("_") == "MajorsWanted":
                    c = MAJOR_CHOICES
                elif field.strip("_") == "DaysAttending":
                    c = DAY_CHOICES
                elif field.strip("_") == "GradeLevelWanted":
                    c = GRADE_LEVEL_CHOICES
                else:
                    c = GRADE_LEVEL_CHOICES
                contains_field = forms.MultipleChoiceField(label=" ",
                    choices=c,
                    widget=forms.CheckboxSelectMultiple(),
                    required=False)
                self.fields["%s_filter" % field_key] = multiple_filter_field
                self.fields["%s_contains" % field_key] = contains_field
            elif field in DATES:
                # A date range to filter by.
                self.fields["%s_filter" % field_key] = date_filter_field
                self.fields["%s_from" % field_key] = forms.DateField(
                    label=" ", widget=SelectDateWidget(), required=False)
                self.fields["%s_to" % field_key] = forms.DateField(
                    label=_("and"), widget=SelectDateWidget(), required=False)
            else:
                # Text box for search term to filter by.
                contains_field = forms.CharField(label=" ", required=False)
                self.fields["%s_filter" % field_key] = text_filter_field
                self.fields["%s_contains" % field_key] = contains_field
        # Add ``FormEntry.entry_time`` as a field.
        field_key = "field_0"
        self.fields["%s_export" % field_key] = forms.BooleanField(initial=True,
            label=" ",
            required=False)
        self.fields["%s_filter" % field_key] = date_filter_field
        self.fields["%s_from" % field_key] = forms.DateField(
            label=" ", widget=SelectDateWidget(), required=False)
        self.fields["%s_to" % field_key] = forms.DateField(
            label=_("and"), widget=SelectDateWidget(), required=False)

    def __iter__(self):
        """
        Yield pairs of include checkbox / filters for each field.
        """
        for field_id in self.form_fields + [0]:
            prefix = "field_%s_" % field_id
            fields = [f for f in super(EntriesForm, self).__iter__()
                      if f.name.startswith(prefix)]

            yield fields[0], fields[1], fields[2:]

    def columns(self):
        """
        Returns the list of selected column names.
        """
        fields = [f for f in self.form_fields
                  if self.cleaned_data["field_%s_export" % f.strip("_")]]

        return fields

    def rows(self, csv=False):
        """
        Returns each row based on the selected criteria.
        """

        # Store the index of each field against its ID for building each
        # entry row with columns in the correct order. Also store the IDs of
        # fields with a type of FileField or Date-like for special handling of
        # their values.
        field_indexes = {}
        file_field_ids = []
        date_field_ids = []
        for field in self.form_fields:
            if self.cleaned_data["field_%s_export" % field.strip("_")]:
                field_indexes[field] = len(field_indexes)
                if field == "picture":
                    file_field_ids.append(field)
        num_columns = len(field_indexes)
        num_columns += 1

        # Get the field entries for the given form and filter by entry_time
        # if specified.
        field_entries = CompanyProfile.objects.all()
        # Loop through each field value ordered by entry, building up each
        # entry as a row. Use the ``valid_row`` flag for marking a row as
        # invalid if it fails one of the filtering criteria specified.
        current_entry = None
        current_row = None
        valid_row = True

        for profile in CompanyProfile.objects.all():
            for field in CompanyProfile._meta.get_fields():
                print field, profile.id
                if profile.id != current_entry:
                    if valid_row and current_row is not None:
                        if not csv:
                            current_row.insert(0, getattr(profile, field.name))
                        yield current_row
                    current_entry = profile.id
                    current_row = [""] * num_columns
                    valid_row = True
                field_value = getattr(profile, field.name)
                field_id = profile.id
                filter_type = "field_%s_filter" % field.name.strip("_")
                filter_args = None
                print "filter type: ", filter_type
                if filter_type:
                    if filter_type == FILTER_CHOICE_BETWEEN:
                        f, t = "field_%s_from" % field.name.strip("_"), "field_%s_to" % field.name.strip("_")
                        filter_args = [f, t]
                else:
                    field_name = "field_%s_contains" % field.name.strip("_")
                    filter_args = field_name
                    if filter_args:
                        filter_args = [filter_args]
                print "Filter_args: ", filter_args
                if filter_args:
                # Convert dates before checking filter.
                    if field_id in date_field_ids:
                        y, m, d = field_value.split(" ")[0].split("-")
                        dte = date(int(y), int(m), int(d))
                        filter_args.append(dte)
                    else:
                        filter_args.append(field_value)
                    filter_func = FILTER_FUNCS[filter_type]
                    print filter_type
                    print filter_func
                    print "filter_args"
                    print filter_args
                    if not filter_func(*filter_args):
                        valid_row = False
                 # Create download URL for file fields.
                if field.name and field_id in file_field_ids:
                    url = reverse("admin:form_file", args=(profile.id,))
                    field_value = self.request.build_absolute_uri(url)
                    if not csv:
                        parts = (field_value, split(field_value)[1])
                        field_value = mark_safe("<a href=\"%s\">%s</a>" % parts)
                # Only use values for fields that were selected.
                try:
                    #print field_indexes
                    #print field.name.strip('_')
                    if isinstance(field_value, list):
                        print field_value
                        field_value = ", ".join(field_value)
                    current_row[field_indexes[field.name.strip('_')]] = str(field_value)
                except KeyError:
                    #print "something bad happened"
                    pass
        # Output the final row.
        if valid_row and current_row is not None:
            if not csv:
                current_row.insert(0, current_entry)
            yield current_row
