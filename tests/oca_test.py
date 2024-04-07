import os
import unittest
import time as T
from oca.client import OCAClient,Observatory,LevelCatalog,Catalog,CatalogItem,ProductFilter, TemporalFilter,InterestFilter,SpatialFilter,Product,Level
import pandas as pd
from concurrent.futures import ThreadPoolExecutor

class TestOCAPI(unittest.TestCase):
    # oca_client = OCAClient(hostname="localhost",port=5000)
    oca_client = OCAClient(hostname="alpha.tamps.cinvestav.mx/ocapi",port=-1)

    @unittest.skip("")
    def test_create_observatory(self):

        res = TestOCAPI.oca_client.create_observatory(
            observatory= Observatory(
                title="Observatorio Hugo",
                description="Observatorio para el Dr. Hugo"
            )
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
        # res = TestOCAPI.oca_client.create_observatory(
        #     observatory= Observatory(title="TEST", description="TEST OBSERVATORY")
        # )
        # self.assertTrue(res.is_ok)
        # obid = res.unwrap()
        # obid = "muolz8dkfkog"
        
        obid = "eos8ql2qlrcg"
        catalogs = [
            LevelCatalog(level=0, cid="iarcgroup59fc8ab669e7"),
            LevelCatalog(level=1, cid="states8ce52701ba74"),
            LevelCatalog(level=2, cid="year20042022"),
        ]
        update_res = TestOCAPI.oca_client.update_observatory_catalogs(
            obid=obid,
            catalogs= catalogs 
        )

# LevelCatalog(level=1, cid="producttypex"),
# ________________________________________
# LevelCatalog(level=0, cid="iz33bpdsfepc3jejsgfll"),
# LevelCatalog(level=1, cid="producttypex"),

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
    
    @unittest.skip("")
    def test_create_catalog_from_json(self):
        # catalog   = Catalog.from_json("/home/nacho/Programming/Python/oca-api/data/iarc_groups_catalog.json")
        # catalog = Catalog.from_json("/home/nacho/Programming/Python/oca-api/data/states_new.json")
        catalog = Catalog.from_json("/home/nacho/Programming/Python/oca-api/data/year_new.json")
        res       = TestOCAPI.oca_client.create_catalog(catalog=catalog)
        print(res)
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
    @unittest.skip("")
    def test_get_catalogs(self):
        res = TestOCAPI.oca_client.get_catalogs()
        return self.assertTrue(res.is_ok)
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
    def test_create_products(self):
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
        ]
        res = TestOCAPI.oca_client.create_products(
            products=products
        )
        return self.assertTrue(res.is_ok)
    
    def delete_product(pid:str)->bool:
        res = TestOCAPI.oca_client.delete_product(pid=pid)
        if res.is_ok:
            print("Product({}) was delete successfully".format(pid))
            return True
        else:
            False
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
