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
    problem = 2

    ret = Start(problem)
    akey = ret['auth_key']
    print('Key is %s' % akey)

    ret = Locations(akey)
    print(ret)

    ret = Trucks(akey)
    print(ret)
    dest = [[0, 0] for _ in range(10)]

    for time in range(240):
        loc = Locations(akey)['locations']

        trk = Trucks(akey)['trucks']
        wtrk = [x for x in trk if x['loaded_bikes_count'] < 3]
        strk = [x for x in trk if x['loaded_bikes_count'] >= 3]

        cmds = []
        # wtrk find sloc
        for wct in wtrk:
            tid = wct['id']
            tlid = wct['location_id']
            tx = tlid // 60
            ty = tlid % 60
            bnt = wct['loaded_bikes_count']
            cmd = []

            if tlid == 3037 or tlid == 3386:
                while len(cmd) < 10 and bnt < 20:
                    bnt += 1
                    cmd.append(5)
                continue
            elif tid%2 == 0:
                lid = 3037
            else:
                lid = 3386

            lx = lid // 60
            ly = lid % 60

            while tx > lx and len(cmd)< 10:
                tx -= 1
                cmd.append(4)
            while tx < lx and len(cmd)< 10:
                tx += 1
                cmd.append(2)
            while ty > ly and len(cmd)< 10:
                ty -= 1
                cmd.append(3)
            while ty < ly and len(cmd)< 10:
                ty += 1
                cmd.append(1)
            while len(cmd) < 10 and bnt < 20:
                bnt += 1
                cmd.append(5)

            cmds.append({"truck_id": tid, "command": cmd})

            # wtrk find sloc
        for sct in strk:
            tid = sct['id']
            tlid = sct['location_id']
            tx = tlid // 60
            ty = tlid % 60
            bnt = sct['loaded_bikes_count']
            cmd = []

            if tlid == 3595 or tlid == 65:
                while len(cmd) < 10 and bnt > 0:
                    bnt += 1
                    cmd.append(6)
                continue
            elif tid % 2 == 0:
                lid = 3595
            else:
                lid = 65

            lx = lid // 60
            ly = lid % 60

            while tx > lx and len(cmd) < 10:
                tx -= 1
                cmd.append(4)
            while tx < lx and len(cmd) < 10:
                tx += 1
                cmd.append(2)
            while ty > ly and len(cmd) < 10:
                ty -= 1
                cmd.append(3)
            while ty < ly and len(cmd) < 10:
                ty += 1
                cmd.append(1)
            while len(cmd) < 10 and bnt > 0:
                bnt += 1
                cmd.append(6)

            cmds.append({"truck_id": tid, "command": cmd})

        ret = Simulate(akey, cmds)
        if time % 10 == 0:
            print('Time: '+str(time)+ ', weakloc: ' + ', Failed: '+ str(ret["failed_requests_count"]))


    ret = Score(akey)
    print(ret)

    for time in range(240, 480):
        loc = Locations(akey)['locations']

        trk = Trucks(akey)['trucks']
        wtrk = [x for x in trk if x['loaded_bikes_count'] < 3]
        strk = [x for x in trk if x['loaded_bikes_count'] >= 3]

        cmds = []
        # wtrk find sloc
        for wct in wtrk:
            tid = wct['id']
            tlid = wct['location_id']
            tx = tlid // 60
            ty = tlid % 60
            bnt = wct['loaded_bikes_count']
            cmd = []

            if tlid == 2635 or tlid == 1320:
                while len(cmd) < 10 and bnt < 20:
                    bnt += 1
                    cmd.append(5)
                continue
            elif tid%2 == 0:
                lid = 2635
            else:
                lid = 1320

            lx = lid // 60
            ly = lid % 60

            while tx > lx and len(cmd)< 10:
                tx -= 1
                cmd.append(4)
            while tx < lx and len(cmd)< 10:
                tx += 1
                cmd.append(2)
            while ty > ly and len(cmd)< 10:
                ty -= 1
                cmd.append(3)
            while ty < ly and len(cmd)< 10:
                ty += 1
                cmd.append(1)
            while len(cmd) < 10 and bnt < 20:
                bnt += 1
                cmd.append(5)

            cmds.append({"truck_id": tid, "command": cmd})

            # wtrk find sloc
        for sct in strk:
            tid = sct['id']
            tlid = sct['location_id']
            tx = tlid // 60
            ty = tlid % 60
            bnt = sct['loaded_bikes_count']
            cmd = []

            if tlid == 724 or tlid == 628:
                while len(cmd) < 10 and bnt > 0:
                    bnt += 1
                    cmd.append(6)
                continue
            elif tid % 2 == 0:
                lid = 724
            else:
                lid = 628

            lx = lid // 60
            ly = lid % 60

            while tx > lx and len(cmd) < 10:
                tx -= 1
                cmd.append(4)
            while tx < lx and len(cmd) < 10:
                tx += 1
                cmd.append(2)
            while ty > ly and len(cmd) < 10:
                ty -= 1
                cmd.append(3)
            while ty < ly and len(cmd) < 10:
                ty += 1
                cmd.append(1)
            while len(cmd) < 10 and bnt > 0:
                bnt += 1
                cmd.append(6)

            cmds.append({"truck_id": tid, "command": cmd})

        ret = Simulate(akey, cmds)
        if time % 10 == 0:
            print('Time: '+str(time)+ ', weakloc: ' + ', Failed: '+ str(ret["failed_requests_count"]))


    ret = Score(akey)
    print(ret)

    for time in range(480, 720):
        loc = Locations(akey)['locations']

        trk = Trucks(akey)['trucks']
        wtrk = [x for x in trk if x['loaded_bikes_count'] < 3]
        strk = [x for x in trk if x['loaded_bikes_count'] >= 3]

        cmds = []
        # wtrk find sloc
        for wct in wtrk:
            tid = wct['id']
            tlid = wct['location_id']
            tx = tlid // 60
            ty = tlid % 60
            bnt = wct['loaded_bikes_count']
            cmd = []

            if tlid == 2465 or tlid == 1571:
                while len(cmd) < 10 and bnt < 20:
                    bnt += 1
                    cmd.append(5)
                continue
            elif tid%2 == 0:
                lid = 2465
            else:
                lid = 1571

            lx = lid // 60
            ly = lid % 60

            while tx > lx and len(cmd)< 10:
                tx -= 1
                cmd.append(4)
            while tx < lx and len(cmd)< 10:
                tx += 1
                cmd.append(2)
            while ty > ly and len(cmd)< 10:
                ty -= 1
                cmd.append(3)
            while ty < ly and len(cmd)< 10:
                ty += 1
                cmd.append(1)
            while len(cmd) < 10 and bnt < 20:
                bnt += 1
                cmd.append(5)

            cmds.append({"truck_id": tid, "command": cmd})

            # wtrk find sloc
        for sct in strk:
            tid = sct['id']
            tlid = sct['location_id']
            tx = tlid // 60
            ty = tlid % 60
            bnt = sct['loaded_bikes_count']
            cmd = []

            if tlid == 969 or tlid == 2233:
                while len(cmd) < 10 and bnt > 0:
                    bnt += 1
                    cmd.append(6)
                continue
            elif tid % 2 == 0:
                lid = 969
            else:
                lid = 2233

            lx = lid // 60
            ly = lid % 60

            while tx > lx and len(cmd) < 10:
                tx -= 1
                cmd.append(4)
            while tx < lx and len(cmd) < 10:
                tx += 1
                cmd.append(2)
            while ty > ly and len(cmd) < 10:
                ty -= 1
                cmd.append(3)
            while ty < ly and len(cmd) < 10:
                ty += 1
                cmd.append(1)
            while len(cmd) < 10 and bnt > 0:
                bnt += 1
                cmd.append(6)

            cmds.append({"truck_id": tid, "command": cmd})

        ret = Simulate(akey, cmds)
        if time % 10 == 0:
            print('Time: '+str(time)+ ', weakloc: ' + ', Failed: '+ str(ret["failed_requests_count"]))


    ret = Score(akey)
    print(ret)

if __name__ == '__main__':
    print('Hello Kakao')
    S0_simulator()