import os
import unittest
import time as T
from oca.client import OCAClient,Observatory,LevelCatalog,Catalog,CatalogItem,ProductFilter, TemporalFilter,InterestFilter,SpatialFilter,Product,Level
import pandas as pd
from concurrent.futures import ThreadPoolExecutor
from uuid import uuid4
from mictlanx.v4.client import Client
from mictlanx.utils.index import Utils

peers =  Utils.routers_from_str(
    routers_str=os.environ.get("MICTLANX_ROUTERS","mictlanx-router-0:alpha.tamps.cinvestav.mx/v0/mictlanx/router:-1"),
    protocol=os.environ.get("MICTLANX_PROTOCOL","https")
) 
# bucket_id = "public-bucket-0"


client = Client(
    client_id       = os.environ.get("CLIENT_ID","melesio-0"),
    routers         = list(peers),
    debug           = True,
    max_workers     = 2,
    bucket_id       = "o5v695jllc3b",
    log_output_path = os.environ.get("MICTLANX_CLIENT_LOG_PATH","/mictlanx/client")
)





class TestOCAPI(unittest.TestCase):

    oca_client = OCAClient(
        hostname="localhost",
        port=5000
    )
    # oca_client = OCAClient(hostname="alpha.tamps.cinvestav.mx/ocapi",port=-1)
    


    @unittest.skip("")
    def test_create_observatory(self):
        res = TestOCAPI.oca_client.create_observatory(
            observatory= Observatory(
                title="Prueba 01",
                description="Deatils"
            )
        )
        return self.assertTrue(res.is_ok)
    

    @unittest.skip("")
    def test_create_catalog_from_json(self):
        # catalog   = Catalog.from_json("/home/nacho/Programming/Python/oca-api/data/iarc_groups_catalog.json")
        # catalog = Catalog.from_json("/home/nacho/Programming/Python/oca-api/data/states_new.json")
        # catalog = Catalog.from_json("/home/nacho/Programming/Python/oca_api/data/year_new.json")
        # catalog = Catalog.from_json("/home/nacho/Programming/Python/oca-client/data/catalogs/years.json")
        # catalog = Catalog.from_json("/home/nacho/Programming/Python/oca-client/data/catalogs/iarc.json")
        # catalog = Catalog.from_json("/home/nacho/Programming/Python/oca-client/data/catalogs/contaminantes.json")
        # catalog = Catalog.from_json("/home/nacho/Programming/Python/oca-client/data/catalogs/product_type.json")
        # catalog = Catalog.from_json("/home/nacho/Programming/Python/oca-client/data/catalogs/states.json")
        # catalog = Catalog.from_json("/home/nacho/Programming/Python/oca-client/data/catalogs/sustancias.json")
        catalog = Catalog.from_json("/home/nacho/Programming/Python/oca-client/data/catalogs/transferencias.json")
        res     = TestOCAPI.oca_client.create_catalog(catalog=catalog)
        print(res)
        return self.assertTrue(res.is_ok)

    @unittest.skip("")
    def test_create_products(self):
        products = [
            Product(
                pid         = "product1x",
                description = "Some description another description......",
                level_path  = "year20042022x",
                profile     = "2004",
                levels=[
                    Level(
                        index=0,
                        cid="year20042022x",
                        value="2004",
                        kind="TEMPORAL"
                    ),
                    # Level(
                    #     index=1,
                    #     cid="producttypex",
                    #     value="MAP",
                    #     kind="INTEREST"
                    # )
                ],
                product_name="Product X",
                product_type="HEATMAP",
            )
        ]
        res = TestOCAPI.oca_client.create_products(
            products=products
        )
        return self.assertTrue(res.is_ok)



    @unittest.skip("")
    def test_delete_observatory(self):
        res = TestOCAPI.oca_client.create_observatory(
            observatory= Observatory(title="TEST", description="TEST OBSERVATORY")
        )
        self.assertTrue(res.is_ok)
        obid = res.unwrap()
        del_res = TestOCAPI.oca_client.delete_observatory(obid=obid)
        return self.assertTrue(del_res.is_ok)
    

    @unittest.skip("")
    def test_update_observatory_catalogs(self):     
        obid = "0z1gdxcb5ne4"

        catalogs = [
            LevelCatalog(level=0, cid="years20042022"),
            LevelCatalog(level=1, cid="iarcgroups"),
            LevelCatalog(level=2, cid="substances"),
            LevelCatalog(level=3, cid="federativeentities"),
            LevelCatalog(level=4, cid="municipios"),
            LevelCatalog(level=5, cid="emisionestransferencias"),
            LevelCatalog(level=6, cid="producttypes"),
            # LevelCatalog(level=1, cid="states8ce52701ba74"),
            # LevelCatalog(level=0, cid="year20042022x"),
        ]
        update_res = TestOCAPI.oca_client.update_observatory_catalogs(
            obid=obid,
            catalogs= catalogs 
        )
        return self.assertTrue(update_res.is_ok)
    
    @unittest.skip("")
    def test_get_observatory(self):
        obid = "csso4ud3tzsqvm03crutrz34"
        res = TestOCAPI.oca_client.get_observatory(obid=obid)
        return self.assertTrue(res.is_ok)
    
    @unittest.skip("")
    def test_get_observatories(self):
        res = TestOCAPI.oca_client.get_observatories(skip=0, limit=10)
        print(res)
        return self.assertTrue(res.is_ok)

    @unittest.skip("")
    def test_create_catalog(self):
        catalog = Catalog(
            cid="",
            display_name="Catalogo",
            items= [
                CatalogItem(
                    value="A",
                    display_name="SUB",
                    code=0,
                    description="A Substance", 
                    metadata={
                        "some":"data"
                    }
                )
            ],
            kind="SOME"
        )
        res = TestOCAPI.oca_client.create_catalog(catalog=catalog)
        return self.assertTrue(res.is_ok)
    

        # catalog = Catalog.from_json("/home/nacho/Programming/Python/oca-api/data/cie_cancer_new.json")

    @unittest.skip("")
    def test_delete_catalog(self):
        catalog = Catalog(
            cid="",
            display_name="Catalogo",
            items= [
                CatalogItem(
                    value="A",
                    display_name="SUB",
                    code=0,
                    description="A Substance", 
                    metadata={
                        "some":"data"
                    }
                )
            ],
            kind="SOME"
        )
        res = TestOCAPI.oca_client.create_catalog(catalog=catalog)
        self.assertTrue(res.is_ok)
        cid = res.unwrap()
        del_res = TestOCAPI.oca_client.delete_catalog(cid = cid)
        return self.assertTrue(del_res.is_ok)
    
    @unittest.skip("")
    def test_get_catalog(self):
        cid = "02es5fdelgtn4zdgglxy5"
        res = TestOCAPI.oca_client.get_catalog(cid = cid)
        return self.assertTrue(res.is_ok)
   
    # @unittest.skip("")
    def test_get_catalogs(self):
        N  = 1000
        t1 = T.time()
        for i in range(N):
            res = TestOCAPI.oca_client.get_catalogs()
        t2 = T.time()
        print(f"Tiempo de prueba: {(t2-t1)/N}")
            # print(response_time)
        # return self.assertTrue(res.is_ok)
        
   
    @unittest.skip("")
    def test_get_products(self):
        res = TestOCAPI.oca_client.get_products(limit=1)
        print(res)
        return self.assertTrue(res.is_ok)

    @unittest.skip("")
    def test_query_products(self):
        obid = "csso4ud3tzsqvm03crutrz34"
        filter = ProductFilter(
            interest=[InterestFilter(
                value="HOMBRES"
            )]
        )
        res = TestOCAPI.oca_client.query_products(obid=obid,filter=filter)
        return self.assertTrue(res.is_ok)


    @unittest.skip("")
    def test_upload_products(self):
        # print("HERE")
        products = []
        for root, folders, files in os.walk("/home/nacho/Programming/Python/oca-client/data/c16"):
            for filename in files:
                # print('UPLOAD', filename)
                xs = filename.split("_")
                x = root.replace("/home/nacho/Programming/Python/oca-client/data/c16/sexo/","").upper().split("/")
                profile = ".".join(x)
                product_path = f"{root}/{filename}"
                bucket_id = "o5v695jllc3bx"
                put_response = client.put_file_chunked(
                    path       = product_path,
                    bucket_id  = bucket_id,
                    chunk_size = "1MB",
                    # key        = "",
                    replication_factor=2,
                    # tags={}
                )
                if put_response.is_err:
                    print("ERROR", put_response)
                    continue
                
                xx = put_response.unwrap()
    
                p = Product(
                    pid=uuid4().hex.replace("-",""),
                    description="No description yet.",
                    level_path="CIE10.SEX.PLOT_TYPE",
                    levels=[
                        Level(
                            cid="cie10c163fb25a076cf021f2",
                            index=0,
                            kind="INTEREST",
                            value="C16",
                        ),
                        Level(
                            cid="sex3fb25a076cf021f2",
                            index=1,
                            kind="INTEREST",
                            value=x[0],

                        ),
                        Level(
                            cid="plottype3fb25a076cf021f2",
                            index=2,
                            kind="INTEREST",
                            value=x[1],
                        )
                    ],
                    product_name="C16 {}".format(profile.replace("."," ")).title(),
                    product_type=x[1],
                    profile=profile,
                    tags=["melesio","o5v695jllc3b"],
                    url=f"https://alpha.tamps.cinvestav.mx/v0/mictlanx/router/api/v4/buckets/{bucket_id}/{xx.key}",
                )
                print("UPLOAD SUCCESSFULLY",p.url)
                products.append(p)
        res = TestOCAPI.oca_client.create_products(
            products=products
        )
        return self.assertTrue(res.is_ok)


    @unittest.skip("")
    def delete_product(pid:str)->bool:
        res = TestOCAPI.oca_client.delete_product(pid=pid)
        if res.is_ok:
            print("Product({}) was delete successfully".format(pid))
            return True
        else:
            False
   
    @unittest.skip("")
    def test_delete_bulk_produs(self):
        df = pd.read_csv("/test/risk_calculator/sink/out_iarcobservatory4.csv")
        with ThreadPoolExecutor(max_workers=4) as tp:
            for i, row in df.iterrows():
                pid = row["pid"]
                tp.submit(TestOCAPI.delete_product,pid)
            # TestOCAPI.oca_client.del
            # print("DELETE",pid)

        return self.assertTrue(True)
    
if __name__ == "__main__":
    unittest.main()
