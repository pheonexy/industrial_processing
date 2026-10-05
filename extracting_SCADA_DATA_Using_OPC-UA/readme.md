OPC UA (Open Platform Communications Unified Architecture) is one of the most common ways to extract data from SCADA systems because it provides a standardized interface between industrial equipment and external applications.

## Typical Architecture
```
Sensors / Machines
        │
        ▼
      PLCs
        │
        ▼
      SCADA
        │
        ▼
  OPC UA Server
        │
        ▼
  OPC UA Client
(Python, Ignition,
Kepware, Airflow,
  Data Collector)
        │
        ▼
Database / Data Lake / Power BI
```
### 1- Identifying the OPC-UA Server:
Most SCADA platforms expose  an OPC-UA server, for exemple:
   Siemens WinCC, AVEVA Wonderware, Ignition, FactoryTalk, Citect SCADA, Kepware
The server exposes industrial tags such as:
```
ns=2;s=Motor1.Speed
ns=2;s=Boiler.Temp
ns=2;s=Tank.Level
```
### 2- Connecting using an OPC-UA Client:
- Install: 
``` pip install opcua ```
- Connect:
[connecting.py](github.com/pheonexy/industrial_processing/extracting_SCADA_DATA_Using_UPC_UA/scripts/upcua_connect.py)
### 3- Get the tree of available tags:
[connecting.py](github.com/pheonexy/industrial_processing/extracting_SCADA_DATA_Using_UPC_UA/scripts/tags_tree.py)

Example of output :
``` 
Objects
├── ProductionLine1
│     ├── Temperature
│     ├── Pressure
│     └── Speed
└── ProductionLine2
      ├── Temperature
      └── FlowRate
```
there are some graphical tools like: 
UaExpert (free) , OPC UA Explorer, Ignition Designer

### 4- Reading Values (Temperature of productionLine1) :
- Showing Boiler temperature:
[connecting.py](github.com/pheonexy/industrial_processing/extracting_SCADA_DATA_Using_UPC_UA/scripts/boiler_temperature_showing.py)
-Collecting Timestamped Data:
[connecting.py](github.com/pheonexy/industrial_processing/extracting_SCADA_DATA_Using_UPC_UA/scripts/collect_timestamped_data.py)
Output: {
"timestamp": "2026-09-30 14:30:00",
"tag": "Boiler.Temp",
"value": 185.4
}
