import json

class DataUtils:

    def site_data(self):
        """
        This function is used to extract data for site datetime A combination of a date and a time. Attributes: ()
        """
        pass

    def site_map_data(self,site_name):

        ##This will return data of websitedatetime A combination of a date and a time. Attributes: ()
        
        f = open('tests/conf_data/site_conf.json')

        site_data = json.load(f)
        return site_data[site_name]

    def data_navigator(self,element_name):
        ##This will return data of navigation details A combination of a date and a time. Attributes: ()
        
        f = open('tests/conf_data/locators.json')

        site_data = json.load(f)
        return site_data[element_name]

