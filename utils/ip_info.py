import requests
import whois




def get_ip_geolocation(ip_address=None):
    """
    Get geolocation data for a given IP address using the Ipify API.
    
    :param ip_address: The IP address to look up. If None, will use the client's public IP.
    :return: JSON data with geolocation information.
    """
    api_key = "at_K7I5j24etIvND4bfHLWeMzhGtVa8V"  # Your API key
    url = f"https://geo.ipify.org/api/v2/country?apiKey={api_key}"

    if ip_address:
        url += f"&ipAddress={ip_address}"

    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Unable to fetch IP geolocation data"}
    
 # Helper function for domain info

    # Using the `whois` library to get domain details
    try:
        domain = whois.whois(domain_name)
        # Return essential domain information
        return {
            "domain": domain_name,
            "registrar": domain.registrar,
            "creation_date": domain.creation_date,
            "expiration_date": domain.expiration_date,
            "name_servers": domain.name_servers
        }
    except Exception as e:
        return {"error": f"Domain lookup failed: {str(e)}"}   



def get_full_domain_info(domain_name):
    try:
        # Fetch the WHOIS data for the domain
        domain_info = whois.whois(domain_name)

        # Return the complete WHOIS information
        return {
            "domain": domain_name,
            "registrar": domain_info.registrar if domain_info.registrar else "Not available",
            "creation_date": domain_info.creation_date if domain_info.creation_date else "Not available",
            "expiration_date": domain_info.expiration_date if domain_info.expiration_date else "Not available",
            "updated_date": domain_info.updated_date if domain_info.updated_date else "Not available",
            "domain_status": domain_info.status if domain_info.status else "Not available",
            "name_servers": domain_info.name_servers if domain_info.name_servers else "Not available",
            "whois_server": domain_info.whois_server if domain_info.whois_server else "Not available",
            "registrant_contact": domain_info.registrant_contact if domain_info.registrant_contact else "Not available",
            "admin_contact": domain_info.admin_contact if domain_info.admin_contact else "Not available",
            "tech_contact": domain_info.tech_contact if domain_info.tech_contact else "Not available",
            "billing_contact": domain_info.billing_contact if domain_info.billing_contact else "Not available"
        }
    except Exception as e:
        return {"error": f"Domain lookup failed: {str(e)}"}

# Example usage


