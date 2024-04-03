import os
import unittest
import time as T
from oca.client import OCAClient,Observatory,LevelCatalog,Catalog,CatalogItem,ProductFilter, TemporalFilter,InterestFilter,SpatialFilter,Product,Level

class TestOCAPI(unittest.TestCase):
    oca_client = OCAClient(hostname="localhost",port=5000)
    @unittest.skip("")
    def test_create_observatory(self):
        res = TestOCAPI.oca_client.create_observatory(
            observatory= Observatory(
                title="Observatorio Melesio",
                description="Observatorio para el Dr. Melesio"
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
        obid = "muolz8dkfkog"
        catalogs = [
            LevelCatalog(level=0, cid="iz33bpdsfepc3jejsgfll")
        ]
        update_res = TestOCAPI.oca_client.update_observatory_calotags(
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
    
    # @unittest.skip("")
    def test_create_catalog_from_json(self):
        catalog = Catalog.from_json("/home/nacho/Programming/Python/oca-api/data/product_types.json")
        res     = TestOCAPI.oca_client.create_catalog(catalog=catalog)
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
                pid="",
                description="DESC",
                level_path="LEVEL1.LEVEL2",
                levels=[
                    Level(
                        index=0,
                        cid="",
                        value="A",
                        kind="SPATIAL"
                    )
                ],
                product_name="PRODUCT_NAME",
                profile="A.B",
                product_type="TYPE",
            )
        ]
        res = TestOCAPI.oca_client.create_products(
            products=products
        )
        return self.assertTrue(res.is_ok)
if __name__ == "__main__":
    unittest.main()
