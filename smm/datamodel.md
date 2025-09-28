# DATA MODEL
Drives design for the app

Legacy lives [here](https://s2m-deylab.in/).


## Research
_Can use leaf pages_
- Hero image `img`
- Entry `[]`
    - Title `str`
    - Description `str`
    - Citation `str[]`
    - URL `str`
    - Thumbnail `img[]`
    - Date `date`

## Publications
_Does not need leaf pages_
- Hero image `img`
- Entry `[]`
    - Authors `str[]`
    - Mentions `str[]`
    - Title `str`
    - Citation `str`
    - URL `str`
    - Year `int`


## Team
_Does not need leaf pages_

_Can be part of the site datamodel_

- Role `str` _(Dropdown: PhD Student/Master Student/...)_
    - Bio `[]`
        - Full name `str`
        - Description `RichText` _(Multiple paras)_
        - Photo `img`
- Alumni
    - Photo `img`
    - Year `int`

> Proposition:
> Use common model with fields as:
> - Full name `str`
> - Role `str`
> - Description `RichText` _(Multiple paras)_
> - Photo `img`
> - Year (Blank, unless alumni)
> 
> Then, use Photo and Year for alumni, and all fields otherwise


## Join
_Does not need leaf pages_

_Can be part of the site datamodel_

- Hero image `img`
- Offering `[]`
    - Name `str`
    - Description `str`
- Email `email`
- Social Media `icon[]`

## Gallery
_Does not need leaf pages_
- Entry `[]`
    - Photo `img`
    - Caption `str`

