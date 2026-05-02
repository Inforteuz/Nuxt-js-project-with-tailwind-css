from rest_framework import serializers
from .models import (
    GeneralInfo, SiteSettings, Banner, NavItem,
    FooterLink, PageSection, SectionCard, MediaAsset
)


class GeneralInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralInfo
        fields = "__all__"


class SiteSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteSettings
        fields = "__all__"


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = "__all__"


class NavItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = NavItem
        fields = "__all__"


class FooterLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterLink
        fields = "__all__"


class SectionCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectionCard
        fields = "__all__"


class PageSectionSerializer(serializers.ModelSerializer):
    cards = SectionCardSerializer(many=True, read_only=True)

    class Meta:
        model = PageSection
        fields = "__all__"


class MediaAssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaAsset
        fields = "__all__"
