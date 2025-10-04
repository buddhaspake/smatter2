from pathlib import Path
import pandas as pd
from django.core.management.base import BaseCommand
from django.core.files import File
from wagtail.images.models import Image as WagtailImage
from base.models.snippets import Publication


PUBLICATIONS_FPATH = "datasheets/publications.csv"
IMAGES_FPATH = "datasheets/images.csv"


def read_tsv(filepath: Path):
    df = pd.read_csv(
        filepath.resolve(),
        sep="\t",
        header=0
    )
    return df


def add_images(root_dir: str):
    df = read_tsv(Path(root_dir) / IMAGES_FPATH)
    df = df.fillna("")
    for row in df.itertuples():
        img_title = row.title
        img_desc = row.description
        img_tags = row.tags
        img_path = Path(root_dir) / row.filepath
        if img_path.is_file():
            with open(img_path, "rb") as imf:
                # Create Django file, and Wagtail Image
                django_file = File(imf, name=img_path.name)
                wt_image = WagtailImage(
                    file=django_file,
                    title=img_title,
                    description=img_desc,
                )
                wt_image.save()
                for tag in img_tags.split(","):
                    wt_image.tags.add(tag.strip())


def add_publications(root_dir: str):
    df = read_tsv(Path(root_dir) / PUBLICATIONS_FPATH)
    pub_objs = (
        Publication(
            topic = row.topic,
            authors = row.authors,
            citation = row.citation,
            year = row.year,
        )
        for row in df.itertuples()
    )
    Publication.objects.bulk_create(pub_objs)


class Command(BaseCommand):
    help = "Add curated data to blog"

    def add_arguments(self, parser):

        parser.add_argument(
            "root",
            help = "Root directory for legacy data",
            type = str,
        )

        parser.add_argument(
            "-c", "--clean",
            help = "Clean existing entries",
            action = "store_true",
        )

    def validate(self, **kwargs):
        if not Path(kwargs["root"]).is_dir():
            raise ValueError(f"Invalid root directory: {kwargs['root']}")

    def handle(self, *args, **kwargs):
        # Validate + read params
        self.validate(**kwargs)
        root_dir = kwargs["root"]
        clean = kwargs["clean"]
        # Clean existing objects if necessary
        if clean:
            Publication.objects.all().delete()
            WagtailImage.objects.all().delete()
        # Pre-load new objects
        add_publications(root_dir)
        add_images(root_dir)

