-- view line 73 of main.lua to see implementation

-- This code is almost parallel to the python implementation,
-- so refer to https://github.com/NanoSmasher/prob-cfvg/TriggerCompare.py for the full documentation

function calculate(a,b,c,d,e,f)			-- Header: Returns the results of calculations
	r = rvr(a,b,c,d,e,f)    v = vrr(a,b,c,d,e,f)	return r[1][1],r[1][2],r[1][3],r[2][1],r[2][2],r[2][3], v[1][1],v[1][2],v[1][3],v[2][1],v[2][2],v[2][3], r[1][4],r[1][5]
end

function vrr(hT,cT,dT,ht,ct,dt)			-- Branch function
    guardrear = v_guardRG(hT,cT,dT,ht,ct,dt)    guardvan = v_guardVG(hT,cT,dT,ht,ct,dt)    return {guardrear,guardvan}
end

function rvr(hT,cT,dT,ht,ct,dt)			-- Branch function
    guardrear = r_guardRG(hT,cT,dT,ht,ct,dt)    guardvan = r_guardVG(hT,cT,dT,ht,ct,dt)    return {guardrear,guardvan}
end

function v_guardVG(hT,cT,dT,ht,ct,dt)	-- Returns expected outcome for VRR and guarding the vanguard attack
    drivecheck = drive(hT,cT,dT)	state = {0,0,0,0,0}    d1 = dmg1(ht,ct,dt)    d2 = dmg2(ht,ct,dt)    d3 = dmg3(ht,ct,dt)
    state[1] = state[1] + d1[1]    state[2] = state[2] + (drivecheck[1][1][1])*(3)    state[2] = state[2] + (drivecheck[1][1][2])*(3)
    state[2] = state[2] + (drivecheck[1][1][3])*(4)    state[2] = state[2] + (drivecheck[1][2][2])*(4)    state[2] = state[2] + (drivecheck[1][2][3])*(4)
    state[2] = state[2] + (drivecheck[1][3][3])*(4)    recover = 0    recover = recover + d1[3]    state[2] = state[2] - recover
    state[3] = state[3] + 3    state[3] = state[3] + (drivecheck[1][1][1])*(2)    state[3] = state[3] + (drivecheck[1][1][2])*(2)
    state[3] = state[3] + (drivecheck[1][1][3])*(2)    state[3] = state[3] + (drivecheck[1][2][2])*(3)    state[3] = state[3] + (drivecheck[1][2][3])*(4)
    state[3] = state[3] + (drivecheck[1][3][3])*(4)    state[3] = state[3] * 5000    state[4] = drivecheck[2]    state[5] = drivecheck[3]    return state
end

function v_guardRG(hT,cT,dT,ht,ct,dt)	-- Returns expected outcome for VRR and guarding both rearguards
    drivecheck = drive(hT,cT,dT)    state = {0,0,0,0,0}    d1 = dmg1(ht,ct,dt)    d2 = dmg2(ht,ct,dt)    d3 = dmg3(ht,ct,dt)    state[1] = state[1] + drivecheck[1][1][4]*d1[1]
    state[1] = state[1] + drivecheck[1][2][4]*d2[1]    state[1] = state[1] + drivecheck[1][3][4]*d3[1]    state[2] = state[2] + (drivecheck[1][1][1])*(2)
    state[2] = state[2] + (drivecheck[1][1][2])*((1-d1[2])*3+d1[2]*2)    state[2] = state[2] + (drivecheck[1][1][3])*(3)    state[2] = state[2] + (drivecheck[1][2][2])*((d2[2][1])*3+(d2[2][2]+d2[2][3])*2)
    state[2] = state[2] + (drivecheck[1][2][3])*((d2[2][1]+d2[2][2])*3+(d2[2][3])*2)    state[2] = state[2] + (drivecheck[1][3][3])*((d3[2][1]+d3[2][2])*3+(d3[2][3]+d3[2][4])*2)
    recover = 0    recover = recover + drivecheck[1][1][4]*d1[3]    recover = recover + drivecheck[1][2][4]*d2[3]    recover = recover + drivecheck[1][3][4]*d3[3]    state[2] = state[2] - recover
    state[3] = state[3] + (drivecheck[1][1][1])*((1-d1[2])*4+d1[2]*2)    state[3] = state[3] + (drivecheck[1][1][2])*((1-d1[2])*5+d1[2]*3)    state[3] = state[3] + (drivecheck[1][1][3])*((1-d1[2])*6+d1[2]*4)
    state[3] = state[3] + (drivecheck[1][2][2])*(d2[2][1]*5+d2[2][2]*3+d2[2][3]*1)    state[3] = state[3] + (drivecheck[1][2][3])*(d2[2][1]*6+d2[2][2]*4+d2[2][3]*2)
    state[3] = state[3] + (drivecheck[1][3][3])*(d3[2][1]*6+d3[2][2]*4+d3[2][3]*2+d3[2][4]*1)    state[3] = state[3] * 5000    state[4] = drivecheck[2]    state[5] = drivecheck[3]    return state
end

function r_guardVG(hT,cT,dT,ht,ct,dt)	-- Returns expected outcome for RVR and guarding the vanguard attack
    drivecheck = drive(hT,cT,dT)    state = {0,0,0,0,0}    d1 = dmg1(ht,ct,dt)    d2 = dmg2(ht,ct,dt)    d3 = dmg3(ht,ct,dt)    state[1] = state[1] + d1[1]
    y = d1[2]    n = 1-d1[2]    state[2] = state[2] + (drivecheck[1][1][1])*(n*3+y*2)    state[2] = state[2] + (drivecheck[1][1][2])*(n*4+y*2)
    state[2] = state[2] + (drivecheck[1][1][3])*(n*4+y*3)    state[2] = state[2] + (drivecheck[1][2][2])*(n*4+y*2)
    state[2] = state[2] + (drivecheck[1][2][3])*(n*4+y*3)    state[2] = state[2] + (drivecheck[1][3][3])*(n*4+y*3)	recover = 0    recover = recover + d1[3]
    state[2] = state[2] - recover    state[3] = state[3] + (drivecheck[1][1][1])*(n*5+y*3)
    state[3] = state[3] + (drivecheck[1][1][2])*(n*6+y*4)    state[3] = state[3] + (drivecheck[1][1][3])*(n*7+y*5)
    state[3] = state[3] + (drivecheck[1][2][2])*(n*6+y*4)    state[3] = state[3] + (drivecheck[1][2][3])*(n*7+y*5)
    state[3] = state[3] + (drivecheck[1][3][3])*(n*7+y*5)    state[3] = state[3] * 5000    state[4] = drivecheck[2]    state[5] = drivecheck[3]    return state
end

function r_guardRG(hT,cT,dT,ht,ct,dt)	-- Returns expected outcome for RVR and guarding the first rearguard attack
    drivecheck = drive(hT,cT,dT)    state = {0,0,0,0,0}    d1 = dmg1(ht,ct,dt)    d2 = dmg2(ht,ct,dt)    d3 = dmg3(ht,ct,dt)    state[1] = state[1] + drivecheck[1][1][4]*d1[1]
    state[1] = state[1] + drivecheck[1][2][4]*d2[1]    state[1] = state[1] + drivecheck[1][3][4]*d3[1]    state[2] = state[2] + 1    state[2] = state[2] + (drivecheck[1][1][1])*(1)
    state[2] = state[2] + (drivecheck[1][1][2])*((1-d1[2])*2+d1[2])    state[2] = state[2] + (drivecheck[1][1][3])*(2)
    state[2] = state[2] + (drivecheck[1][2][2])*((d2[2][1])*2+(d2[2][2]+d2[2][3])*1)    state[2] = state[2] + (drivecheck[1][2][3])*((d2[2][1]+d2[2][2])*2+(d2[2][3])*1)
    state[2] = state[2] + (drivecheck[1][3][3])*((d3[2][1]+d3[2][2])*2+(d3[2][3]+d3[2][4])*1)    recover = 0    recover = recover + drivecheck[1][1][4]*d1[3] 
	recover = recover + drivecheck[1][2][4]*d2[3]    recover = recover + drivecheck[1][3][4]*d3[3]    state[2] = state[2] - recover    state[3] = state[3] + 2
    state[3] = state[3] + (drivecheck[1][1][1])*((1-d1[2])*2+d1[2]*1)    state[3] = state[3] + (drivecheck[1][1][2])*((1-d1[2])*3+d1[2]*2)
    state[3] = state[3] + (drivecheck[1][1][3])*((1-d1[2])*4+d1[2]*3)    state[3] = state[3] + (drivecheck[1][2][2])*(d2[2][1]*3+d2[2][2]*2+d2[2][3]*1)
    state[3] = state[3] + (drivecheck[1][2][3])*(d2[2][1]*4+d2[2][2]*3+d2[2][3]*2)    state[3] = state[3] + (drivecheck[1][3][3])*(d3[2][1]*4+d3[2][2]*3+d3[2][3]*2+d3[2][4]*1)
    state[3] = state[3] * 5000    state[4] = drivecheck[2]    state[5] = drivecheck[3]    return state
end

function drive(hT,cT,dT)				-- Returns values for the twin drive
    hThT = (hT/49)*((hT-1)/48)    hTcT = (hT/49)*(cT/48)+(cT/49)*(hT/48)    hTdT = (hT/49)*(dT/48)+(dT/49)*(hT/48)    hTnT = (hT/49)*(33/48)+(33/49)*(hT/48)
	cTcT = (cT/49)*((cT-1)/48)    cTdT = (cT/49)*(dT/48)+(dT/49)*(cT/48)    cTnT = (cT/49)*(33/48)+(33/49)*(cT/48)    dTdT = (dT/49)*((dT-1)/48)    dTnT = (dT/49)*(33/48)+(33/49)*(dT/48)
    nTnT = (22/49)    dmgstg = {}    dmgstg[1] = {nTnT, dTnT+hTnT, dTdT+hTdT+hThT, nTnT+dTnT+hTnT+dTdT+hTdT+hThT}    dmgstg[2] = {0, cTnT, hTcT+cTdT, cTnT+hTcT+cTdT}
	dmgstg[3] = {0,0,cTcT,cTcT}    dmgh = 2*hThT + hTcT+hTdT+hTnT    drw = 2*dTdT + hTdT+cTdT+dTnT    return {dmgstg,dmgh,drw}
end

function dmg1(ht,ct,dt)					-- Returns values for the event when 1 damage is taken
    return {(49-ht)/49 , 16/49 , dt/49}
end

function dmg2(ht,ct,dt)					-- Returns values for the event when 2 damage is taken
	dmg = 0    sld = {}    hin = 0    nt=33    htht = (ht/49)*((ht-1)/48)    htct = (ht/49)*(ct/48) + (ct/49)*(ht/48)    htdt = (ht/49)*(dt/48) + (dt/49)*(ht/48)
	htnt = (ht/49)*(nt/48) + (nt/49)*(ht/48)    ctct = (ct/49)*((ct-1)/48)    ctdt = (ct/49)*(dt/48) + (dt/49)*(ct/48)    ctnt = (ct/49)*(nt/48) + (nt/49)*(ct/48)
	dtdt = (dt/49)*((dt-1)/48)    dtnt = (dt/49)*(nt/48) + (nt/49)*(dt/48)    ntnt = (nt/49)*((nt-1)/48)    dmg = dmg + 2*(ctct+ctdt+ctnt+dtdt+dtnt+ntnt)	dmg = dmg + 1*(htct+htdt+htnt)
	sld[1] = (ntnt)    sld[2] = (htnt+ctnt+dtnt)    sld[3] = (htht+htct+htdt+ctct+ctdt+dtdt) hin = 2*(dtdt) + 1*(htdt+ctdt+dtnt)    return {dmg, sld, hin}
end

function dmg3(ht,ct,dt)					-- Returns values for the event when 3 damage is taken
	dmg = 0    sld = {}    hin = 0    nt=33    hththt = (ht/49)*((ht-1)/48)*((ht-2)/47)    hthtct = (ht/49)*((ht-1)/48)*(ct/47) + (ht/49)*(ct/48)*((ht-1)/47) + (ct/49)*(ht/48)*((ht-1)/47)
    hthtdt = (ht/49)*((ht-1)/48)*(dt/47) + (ht/49)*(dt/48)*((ht-1)/47) + (dt/49)*(ht/48)*((ht-1)/47)    hthtnt = (ht/49)*((ht-1)/48)*(nt/47) + (ht/49)*(nt/48)*((ht-1)/47) + (nt/49)*(ht/48)*((ht-1)/47)
    htctct = (ct/49)*((ct-1)/48)*(ht/47) + (ct/49)*(ht/48)*((ct-1)/47) + (ht/49)*(ct/48)*((ct-1)/47)
    htctdt = (ht/49)*(ct/48)*(dt/47) + (ht/49)*(dt/48)*(ct/47) + (ct/49)*(ht/48)*(dt/47) + (ct/49)*(dt/48)*(ht/47) + (dt/49)*(ht/48)*(ct/47) + (dt/49)*(ht/48)*(ct/47)
    htctnt = (ht/49)*(ct/48)*(nt/47) + (ht/49)*(nt/48)*(ct/47) + (ct/49)*(ht/48)*(nt/47) + (ct/49)*(nt/48)*(ht/47) + (nt/49)*(ht/48)*(ct/47) + (nt/49)*(ht/48)*(ct/47)
    htdtdt = (dt/49)*((dt-1)/48)*(ht/47) + (dt/49)*(ht/48)*((dt-1)/47) + (ht/49)*(dt/48)*((dt-1)/47)
    htdtnt = (ht/49)*(dt/48)*(nt/47) + (ht/49)*(nt/48)*(dt/47) + (dt/49)*(ht/48)*(nt/47) + (dt/49)*(nt/48)*(ht/47) + (nt/49)*(ht/48)*(dt/47) + (nt/49)*(ht/48)*(dt/47)
    htntnt = (nt/49)*((nt-1)/48)*(ht/47) + (nt/49)*(ht/48)*((nt-1)/47) + (ht/49)*(nt/48)*((nt-1)/47)
    ctctct = (ct/49)*((ct-1)/48)*((ct-2)/47)    ctctdt = (ct/49)*((ct-1)/48)*(dt/47) + (ct/49)*(dt/48)*((ct-1)/47) + (dt/49)*(ct/48)*((ct-1)/47)
    ctctnt = (ct/49)*((ct-1)/48)*(nt/47) + (ct/49)*(nt/48)*((ct-1)/47) + (nt/49)*(ct/48)*((ct-1)/47)    ctdtdt = (dt/49)*((dt-1)/48)*(ct/47) + (dt/49)*(ct/48)*((dt-1)/47) + (ct/49)*(dt/48)*((dt-1)/47)
    ctdtnt = (ct/49)*(dt/48)*(nt/47) + (ct/49)*(nt/48)*(dt/47) + (dt/49)*(ct/48)*(nt/47) + (dt/49)*(nt/48)*(ct/47) + (nt/49)*(ct/48)*(dt/47) + (nt/49)*(ct/48)*(dt/47)
    ctntnt = (nt/49)*((nt-1)/48)*(ct/47) + (nt/49)*(ct/48)*((nt-1)/47) + (ct/49)*(nt/48)*((nt-1)/47)
    dtdtdt = (dt/49)*((dt-1)/48)*((dt-2)/47)    dtdtnt = (dt/49)*((dt-1)/48)*(nt/47) + (dt/49)*(nt/48)*((dt-1)/47) + (nt/49)*(dt/48)*((dt-1)/47)
    dtntnt = (nt/49)*((nt-1)/48)*(dt/47) + (nt/49)*(dt/48)*((nt-1)/47) + (dt/49)*(nt/48)*((nt-1)/47)    ntntnt = (nt/49)*((nt-1)/48)*((nt-2)/47)
	dmg = dmg + 3*(ctctct+ctctdt+ctctnt+ctdtdt+ctdtnt+ctntnt+dtdtdt+dtdtnt+dtntnt+ntntnt)    dmg = dmg + 2*(htctct+htctdt+htctnt+htdtdt+htdtnt+htntnt)    dmg = dmg + 1*(hthtct+hthtdt+hthtnt)
    sld[1] = (ntntnt)    sld[2] = (htntnt+dtntnt+ctntnt)    sld[3] = (hthtnt+htctnt+htdtnt+ctctnt+ctdtnt+dtdtnt)
    sld[4] = (hththt+hthtct+hthtdt+htctct+htctdt+htdtdt+ctctct+ctctdt+ctdtdt+dtdtdt)    hin = 3*(dtdtdt) + 2*(htdtdt+ctdtdt+dtdtnt) + 1*(hthtdt+htctdt+htdtnt+ctctdt+ctdtnt+dtntnt)    return {dmg, sld, hin}
end
