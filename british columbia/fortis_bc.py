import json
import requests
import xml.etree.ElementTree as ET

url = "https://outages.fortisbc.com/outages/Home/UpdatePushpin"

def fetch_outage_data():
    try:
        response = requests.get(url)
        if response.status_code == 200:
            root = ET.fromstring(response.content)
            outage_list = []
            for oms_case in root.findall('OMSCASES'):
                outage_details = {
                    'serial': oms_case.find('SERIAL').text,
                    'description': oms_case.find('DESC').text,
                    'notes': oms_case.find('NOTES').text,
                    'planned': oms_case.find('PLANNED').text,
                    'casestatus': oms_case.find('CASESTAT').text,
                    'workstatus': oms_case.find('WORKSTAT').text,
                    'latitude': oms_case.find('AVGLAT').text,
                    'longitude': oms_case.find('AVGLONG').text,
                    'outage_time': oms_case.find('OUTTIME').text,
                    'initial_customers': oms_case.find('INITCUST').text,
                    'current_customers': oms_case.find('CURCUST').text,
                    'restore_time': oms_case.find('RESTORETIM').text,
                    'restore_range': oms_case.find('RESTRANGE').text,
                    'cause': oms_case.find('DESC_CAUSE').text,
                    'coordinates_list': oms_case.find('COORDLIST').text
                }
                outage_list.append(outage_details)

            return outage_list
        else:
            return None
    except (ET.ParseError, Exception) as e:
        print(f"Error fetching data: {e}")
        return None

if __name__ == "__main__":
    outage_data = fetch_outage_data()
    print(json.dumps(outage_data, indent=2) if outage_data else "[]")
