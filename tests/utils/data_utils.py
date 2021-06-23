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

    # def option(self):
    #     self.site_name = "golocal"
    #     self.locator_name = "gender"
    #     _opt_data = self.site_map_data(self.site_name) #male or female.
    #     opt_data = _opt_data["gender"]
    #     _loc = self.data_navigator(self.site_name)

    #     _loc_value = _loc[self.locator_name]

    #     print(_loc_value[opt_data])


# obj = DataUtils()
# obj.option()




