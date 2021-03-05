import requests

url = 'https://pegkq2svv6.execute-api.ap-northeast-2.amazonaws.com/prod/users'

def Start(problem):
    uri = url + '/start'
    return requests.post(uri, headers={'X-Auth-Token': '44b9b0a600ffb009fddcf46af60e3aaf'}, json={'problem': problem}).json()


def Locations(akey):
    uri = url + '/locations'
    return requests.get(uri, headers={'Authorization': akey}).json()

def Trucks(akey):
    uri = url + '/trucks'
    return requests.get(uri, headers={'Authorization': akey}).json()

def Simulate(akey, cmds):
    uri = url + '/simulate'
    return requests.put(uri, headers={'Authorization': akey}, json={'commands': cmds}).json()

def Score(akey):
    uri = url + '/score'
    return requests.get(uri, headers={'Authorization': akey}).json()

def S0_simulator():
    problem = 1

    ret = Start(problem)
    akey = ret['auth_key']
    print('Key is %s' % akey)

    ret = Locations(akey)
    print(ret)

    ret = Trucks(akey)
    print(ret)

    for time in range(720):
        loc = Locations(akey)['locations']
        wloc = [x for x in loc if x['located_bikes_count'] < 2]
        sloc = [x for x in loc if x['located_bikes_count'] > 2]
        trk = Trucks(akey)['trucks']
        wtrk = [x for x in trk if x['loaded_bikes_count'] < 1]
        strk = [x for x in trk if x['loaded_bikes_count'] >= 1]

        cmds = []
        #wtrk find sloc
        for wct in wtrk:
            tid = wct['id']
            tlid = wct['location_id']
            tx = tlid // 5
            ty = tlid % 5
            bnt = wct['loaded_bikes_count']
            cmd = []

            #while sloc:
            if len(sloc) == 0: break
            scl = sloc.pop()
            lid = scl['id']
            lx = lid // 5
            ly = lid % 5
            bn = scl['located_bikes_count']

            while tx > lx:
                tx -= 1
                cmd.append(4)
            while tx < lx:
                tx += 1
                cmd.append(2)
            while ty > ly:
                ty -= 1
                cmd.append(3)
            while ty < ly:
                ty += 1
                cmd.append(1)
            while bn > 2 and len(cmd) < 10 and bnt < 5:
                bn -= 1
                bnt += 1
                cmd.append(5)

            cmds.append({"truck_id": tid, "command": cmd})

        #strk find wloc
        for sct in strk:
            tid = sct['id']
            tlid = sct['location_id']
            tx = tlid // 5
            ty = tlid % 5
            bnt = sct['loaded_bikes_count']
            cmd = []

            #while wloc:
            if len(wloc) == 0: break
            wcl = wloc.pop()
            lid = wcl['id']
            lx = lid // 5
            ly = lid % 5
            bn = wcl['located_bikes_count']

            while tx > lx:
                tx -= 1
                cmd.append(4)
            while tx < lx:
                tx += 1
                cmd.append(2)
            while ty > ly:
                ty -= 1
                cmd.append(3)
            while ty < ly:
                ty += 1
                cmd.append(1)
            while bn < 2 and len(cmd) < 10 and bnt > 0:
                bnt -= 1
                bn += 1
                cmd.append(6)

            cmds.append({"truck_id": tid, "command": cmd})

        ret = Simulate(akey, cmds)
        if time % 10 == 0:
            print('Time: '+str(time)+ ', weakloc: '+ str(len(wloc)) + ', Failed: '+ str(ret["failed_requests_count"]))


    ret = Score(akey)
    print(ret)

if __name__ == '__main__':
    print('Hello Kakao')
    S0_simulator()