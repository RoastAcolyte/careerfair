/home/ruben/careerfair/static
BEGIN;
DELETE FROM "auth_permission";
DELETE FROM "theme_featuredcompany";
DELETE FROM "forms_formentry";
DELETE FROM "theme_staffprofile";
DELETE FROM "theme_armorytabledata";
DELETE FROM "generic_assignedkeyword";
DELETE FROM "blog_blogcategory";
DELETE FROM "generic_rating";
DELETE FROM "django_site";
DELETE FROM "core_sitepermission_sites";
DELETE FROM "auth_group";
DELETE FROM "django_comment_flags";
DELETE FROM "theme_sponsorshippackage";
DELETE FROM "django_content_type";
DELETE FROM "django_session";
DELETE FROM "theme_paypalinfo";
DELETE FROM "pages_link";
DELETE FROM "core_sitepermission";
DELETE FROM "auth_user_groups";
DELETE FROM "galleries_galleryimage";
DELETE FROM "theme_companyprofile";
DELETE FROM "theme_sponsoruspage";
DELETE FROM "auth_user_user_permissions";
DELETE FROM "generic_keyword";
DELETE FROM "twitter_query";
DELETE FROM "pages_richtextpage";
DELETE FROM "theme_announcement";
DELETE FROM "galleries_gallery";
DELETE FROM "theme_registrationpage";
DELETE FROM "django_redirect";
DELETE FROM "theme_question";
DELETE FROM "auth_group_permissions";
DELETE FROM "theme_agendapage";
DELETE FROM "forms_form";
DELETE FROM "theme_faqpage";
DELETE FROM "conf_setting";
DELETE FROM "blog_blogpost_categories";
DELETE FROM "generic_threadedcomment";
DELETE FROM "theme_companyrep";
DELETE FROM "pages_page";
DELETE FROM "paypal_nvp";
DELETE FROM "django_admin_log";
DELETE FROM "theme_iconblurb";
DELETE FROM "django_comments";
DELETE FROM "forms_fieldentry";
DELETE FROM "theme_contactpage";
DELETE FROM "theme_slide";
DELETE FROM "theme_aboutpage";
DELETE FROM "theme_studentsearchformmodel";
DELETE FROM "paypal_ipn";
DELETE FROM "theme_pricingpage";
DELETE FROM "blog_blogpost_related_posts";
DELETE FROM "blog_blogpost";
DELETE FROM "theme_homepage";
DELETE FROM "auth_user";
DELETE FROM "twitter_tweet";
DELETE FROM "forms_field";
DELETE FROM "theme_studentprofile";

COMMIT;