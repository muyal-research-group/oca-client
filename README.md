# OCA-Client : Client for observatory management 


## Getting started

We must create the ```Catalog``` object before creating a new ```Observatory```:

```python
class Catalog(BaseModel):
    cid:str = ""
    display_name:str = ""
    items: List[CatalogItem] = []
    kind:str = ""
class CatalogItem(BaseModel):
    value:str
    display_name:str
    code:int
    description:str
    metadata:Dict[str,str]
````

An catalog has many items with the ```CatalogItem``` object definition. You can create an new ```Catalog``` using the oca client, we can create a new oca client using the next code:
```python
from oca.client import OCAClient
oca_client = OCAClient(hostname="localhost",port=5000)
```
⚠️ remember to deploy an instance of oca api the step by step guide is [here](https://github.com/muyal-research-group/oca_api)


Using this instance of ```OCAClient```, we can create a ```Catalog``` object:

```python
from oca.client import Catalog,OCAClient
# Edit the attributes as you need
catalog = Catalog(
    cid="",
    display_name="",
    items= [
        CatalogItem(
            value="",
            display_name="",
            code=0,
            description="", 
            metadata={
               
            }
        )
    ],
    kind="SOME"
)
response = oca_client.create_catalog(
    catalog = catalog
)
response.is_ok # => if True the creation was successfully
```

Now we are ready to create main object in this model, an  ```Observatory``` defined as follows:
```python
class Observatory(BaseModel):
    obid:str                    = ""
    title: str                  = ""
    image_url:str               = ""
    description:str             = ""
    catalogs:List[LevelCatalog] = []
    disabled:bool               = False
```

An observatory can contains many catalogs, expressed in the form of a list of catalogs  ```catalogs:List[LevelCatalog]```  in the ```Observatory``` object definition:

```python
class LevelCatalog(BaseModel):
    level: int
    cid: str
```
we can create an ```Observatory``` using the client:

```python
import oca.client import OCAClient,Observatory,LevelCatalog

# edit the attribute as you need..
observatory = Observatory(
    obid        = ""
    title       = ""
    image_url   = ""
    description = ""
    catalogs    = [
        LevelCatalog(
            level = 0,
            cid="firstcatalog"
        )
    ]
    disabled    = False
)

oca_client.create_observatory(observatory = observatory)
```

⚠️ The attribute ```disabled``` manage the visibility of the observatory object, you can disabled and this observatory disappers without deleting the object. 

Finally we have object definition of the ```Product```: 

```python
class Product(BaseModel):
    pid:str=""
    description:str=""
    levels:List[Level]=[]
    product_type: str=""
    level_path:str=""
    profile:str=""
    product_name: str=""
    tags:List[str]=[]
    url:str =""
class Level(BaseModel):
    index:int
    cid:str
    value:str
    kind:str =""

```

we can create multiples products using the next method:
```python
from oca.client import Product, Level

products = [
     Product(
                pid="product1",
                description="Some description",
                level_path="iz33bpdsfepc3jejsgfll.producttypex",
                levels=[
                    Level(
                        index=0,
                        cid="iz33bpdsfepc3jejsgfll",
                        value="C00",
                        kind="INTEREST"
                    ),
                    Level(
                        index=1,
                        cid="producttypex",
                        value="MAP",
                        kind="INTEREST"
                    )
                ],
                product_name="Product 1",
                profile="C00.MAP",
                product_type="PRODUCT",
            )    
            # .....
]

response = oca_client.create_products(
    products = products
)
```






## Prerequisites 

You only gonna need the next python library:
```sh
pip install -i https://test.pypi.org/simple/ goca==0.0.2
```

and for package managing and distribution install ```Poetry``` [here](https://python-poetry.org/):

```sh
pip3 install poetry
```

## Development

For development purposes you need to clone this repo:

```sh
git clone git@github.com:muyal-research-group/oca-client.git
```

After you clonning the repo, you must navigate to the ```oca-client``` folder:
```sh
cd oca-client
```

Now you should activating the virtualenv:

```sh
poetry shell
```

Then you should install the dependencies:
```sh
poetry install
```

Now you can run the test in the ````tests/``` folder: 

```sh
python3 tests/oca_test.sh
```

⚠️ Please check the ```oca_file.py``` after run to skip manually some of the tests.


## Building and Publishing

When you are done with the features you need to build the project: 

```sh
poetry build
```

Then you should execute the next command:

```sh
poetry publish -r ocatestpypi
```

:warning: Before publishing you must set up the tokens in the ```~/.config/pypoetry/auth.toml``` path. 



## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

 Ignacio Castillo - [@NachoCastillo]() - jesus.castillo.b@cinvestav.mx

<p align="right">(<a href="#top">back to top</a>)</p>






