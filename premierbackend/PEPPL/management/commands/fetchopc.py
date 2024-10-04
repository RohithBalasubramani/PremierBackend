# energy/management/commands/fetch_opc_data.py

from django.core.management.base import BaseCommand
from opcua import Client
from django.utils import timezone
from energy.models import *

class Command(BaseCommand):
    help = 'Fetch data from OPC UA server and store in the database'

    def handle(self, *args, **kwargs):
        url = "opc.tcp://<your_opc_server>:<port>"
        client = Client(url)
        
        try:
            client.connect()
            global_vars_node = client.get_node("ns=9;s=/.GlobalVars")
            
            # Define a dictionary to map OPC tags to model fields
            tag_model_mapping = {
                "NS14[STRINq]/q.HT2_MFM1_FREQ": ("P1_PepplHT_OutGoing1", "freq"),
                "NS14[STRINq]/q.HT2_MFM2_FREQ": ("P1_PepplHT_OutGoing2", "freq"),
                "NS14[STRINq]/q.HT2_MFM3_FREQ": ("P1_PepplHT_OutGoing3", "freq"),
                "NS14[STRINq]/q.HT2_MFM4_FREQ": ("P1_PepplHT_OutGoing4", "freq"),
                "NS14[STRINq]/q.HT2_MFM5_FREQ": ("P1_PepplHT_HTPanelIncomer", "freq"),
            }

            # Fetch and store data
            for tag, model_class in tag_model_mapping.items():
                node = global_vars_node.get_child(f"{tag}")
                value = node.get_value()

                # Create or update the corresponding model instance
                model_instance, created = model_class.objects.update_or_create(
                    timestamp=timezone.now(),
                    defaults={tag.split("_", 1)[1].lower(): value}
                )

                if created:
                    self.stdout.write(self.style.SUCCESS(f"Created new entry for {tag}"))
                else:
                    self.stdout.write(self.style.SUCCESS(f"Updated entry for {tag}"))

        except Exception as e:
            self.stderr.write(f"Error fetching data from OPC UA server: {e}")
        finally:
            client.disconnect()
