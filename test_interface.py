#!/usr/bin/python3
#Rolling release version.
#Purpose: Testing configuring interface ip address.
#

def conn():

        iface= ["interfaces", "ethernet", "eth1", "address"]

        try:
                #Connecting to session.
                conn_session = vyos.configsession.ConfigSession(os.getpid())

                #Setting up interface ip address.
                conn_session.set(iface, value= "10.0.0.1/24")

                #Commit configuration.
                conn_session.commit()

                #Show interface configuration.
                print(conn_session.show("interfaces"))

        except ConfigSessionError as err:
                raise err

conn()
