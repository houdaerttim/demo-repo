def isOracleUser(user_id):
    s = "oraxs1"
    if not(len(s) == 6 and s.find("ora",0,3) == 0) :
        return False
        #(f" {s} is not an oracle user")
    else:
        return True
        #(f"Ok go, {s} is an Oracle User")