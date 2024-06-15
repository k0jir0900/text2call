# Text2Call

Este proyecto permite generar una llamada telefónica que reproduciendo un audio “custom” cuando se responde el llamado. El audio se genera a partir de un texto, este se convierte en un audio .GSM y luego se reproduce en una llamada realizada a través de una PBX SIP.

## Requisitos

- Python 3.x
- Asterisk
- Sox (Sound eXchange)

## Instalación

1. Clonar el repositorio:

   ```sh
   git clone https://github.com/k0jir0900/text2call.git 
   cd text2call
   ```

2. Instalar las dependencias:

    ```bash
    pip3 install -r requirements.txt
    ```

## Uso
Ejecutar el script con un argumento de texto que deseas convertir en un mensaje de voz y realizar la llamada:

### notification.py
Este script se debe utilizar cuando el anexo al que se notificará se encuentra en la misma PBX. 

1. Define el número de anexo al cual realizaras la llamada:
    ```python
    anexo = '{número anexo}'
    ```

2. Define el nombre y número de anexo que realizará la llamada:
    ```python
    caller_id = '{nombre anexo <número saliente>}'

3. Ejecuta el script:
    ```bash
    python3 notification.py "<texto>"
    ```

### notification_siptrunk.py
Este script se debe utilizar cuando la llamada se realice a otra PBX o hacía la PSTN. 

1. Define el número de anexo al cual realizaras la llamada:
    ```python
    anexo = '{número anexo}'
    ```

2. Define el nombre y número de anexo que realizará la llamada:
    ```python
    caller_id = '{nombre anexo <número saliente>}'
    ```

3. Define el nombre del SIP Trunk por donde saldrá la llamada:
    ```python
    sip_trunk = '{nombre SIP TRUNK}'
    ```    

4. Ejecuta el script:
    ```bash
    python3 notification_siptrunk.py "<texto>"
    ```