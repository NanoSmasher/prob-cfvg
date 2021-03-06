require "trigcompare"
-- The actual heavy work

-- love.load			:	load variables and initializes object and static
-- object 				:	information about the buttons and button locations
-- static 				:	static text labels
-- input & output 		:	display text labels that change based on events.
-- love.keyreleased 	:	[Esc]  to quit the program easily, [C] to copy result onto Clipboard
-- love.draw 			:	Draws all the stuff
-- love.mousepressed	:	Changes the input and output.
-- sethover				:	determines whether the click of {mousepressed} matches with an {object} bounds

function love.load()
	love.window.setMode(700,400)
	love.window.setTitle("Trigger Advantage Comparison - Created by Brampton Booster")
	screen = 'main'
	changed = true

	--Constants for table-like organization
	newrow = 30		newcol = 150	
	
	--numbers used for calculations
	ycrit = 12	yheal = 4	ydraw = 0
	fcrit = 12	fheal = 4	fdraw = 0
	
	--numbers resulting from calculations
	dam1 = '0'	car1 = '0'	shi1 = '0'
	dam2 = '0'	car2 = '0'	shi2 = '0'
	dam3 = '0'	car3 = '0'	shi3 = '0'
	dam4 = '0'	car4 = '0'	shi4 = '0'
	heal = '0'	gain = '0'	err = ''
	
	--initialize the other stuff
	object()
	static()
end

function love.keyreleased(key)
	if key == "escape" then love.event.push("quit") end
	if (key == "c" and changed == false) then love.system.setClipboardText(

ycrit..'C/'..yheal..'H/'..ydraw.."D vs "..fcrit..'C/'..fheal..'H/'..fdraw.."D \n"..
[[
Attack Plan		Defensive Measure	Damage	Cards	Shield
R>V>R			Let VG Through		]]..string.format("%.5f", dam1)..string.format("	%.4f", car1)..string.format("	%.0f", shi1)..[[

R>V>R			Let RG Through		]]..string.format("%.5f", dam2)..string.format("	%.4f", car2)..string.format("	%.0f", shi2)..[[ 
V>R>R			Let VG Through		]]..string.format("%.5f", dam3)..string.format("	%.4f", car3)..string.format("	%.0f", shi3)..[[

V>R>R			Let RG Through		]]..string.format("%.5f", dam4)..string.format("	%.4f", car4)..string.format("	%.0f", shi4)..[[

Damage you heal]]..string.format("	%.5f", heal)..[[

Cards you draw]]..string.format("	%.4f", gain).."\n \n (c) bramptonbooster.wordpress.com"
) end

end

function love.draw()
	love.graphics.draw(staticcanvas, 0, 0)		-- draw static text
	if (changed == false) then output() end		-- draw output if the input hasn't changed
	input() 									-- draw user input
	love.graphics.setColor(255,255,255)
end

function love.mousepressed(x, y, b)
	if (b == "l" and screen == 'main') then
		--figure out if the cursor is over a button and if so which one
		local on = sethover(x,y)
		
		--huge conditional branch
		if 	   (on=='none')   then return
								--can't be past 16
		elseif (on=='ycrit+' and ycrit+yheal+ydraw<16) then ycrit = ycrit + 1 changed = true
		elseif (on=='yheal+' and ycrit+yheal+ydraw<16) then yheal = yheal + 1 changed = true
		elseif (on=='ydraw+' and ycrit+yheal+ydraw<16) then ydraw = ydraw + 1 changed = true
		elseif (on=='fcrit+' and fcrit+fheal+fdraw<16) then fcrit = fcrit + 1 changed = true
		elseif (on=='fheal+' and fcrit+fheal+fdraw<16) then fheal = fheal + 1 changed = true
		elseif (on=='fdraw+' and fcrit+fheal+fdraw<16) then fdraw = fdraw + 1 changed = true
								--can't be negative
		elseif (on=='ycrit-' and ycrit>0) then ycrit = ycrit - 1 changed = true
		elseif (on=='yheal-' and yheal>0) then yheal = yheal - 1 changed = true
		elseif (on=='ydraw-' and ydraw>0) then ydraw = ydraw - 1 changed = true
		elseif (on=='fcrit-' and fcrit>0) then fcrit = fcrit - 1 changed = true
		elseif (on=='fheal-' and fheal>0) then fheal = fheal - 1 changed = true
		elseif (on=='fdraw-' and fdraw>0) then fdraw = fdraw - 1 changed = true
		elseif (on=='enter')  then
			if (ycrit+yheal+ydraw==16 and fcrit+fheal+fdraw==16) then
				--the very very long fetch
				dam1,car1,shi1,dam2,car2,shi2,dam3,car3,shi3,dam4,car4,shi4,heal,gain = calculate(yheal,ycrit,ydraw,fheal,fcrit,fdraw)			
				changed = false
				err = ''
			else err = 'ERROR' end
		elseif (on=='about')  then screen = 'about'
		end
		
		input()
		output()
	
	--close the about screen
	elseif (b == "l" and screen == 'about') then screen = 'main'
	end
end

function sethover(getx,gety)
	for i = 1, #button do
		if (getx>=button[i].x1 and getx<=button[i].x2 and gety>=button[i].y1 and gety<=button[i].y2) then
			return button[i].name
		end
	end
	return 'none'
end

function object()
	img_up = love.graphics.newImage("Up.bmp")
	img_dw = love.graphics.newImage("Down.bmp")
	img_en = love.graphics.newImage("Enter.bmp")
	img_ab = love.graphics.newImage("Q.bmp")	
	
	button = {
		{name = "ycrit+",	x1 = newcol+30,		y1 = newrow,	x2 = newcol+42,		y2 = newrow+12},
		{name = "yheal+",	x1 = 2*newcol+30,	y1 = newrow,	x2 = 2*newcol+42,	y2 = newrow+12},
		{name = "ydraw+",	x1 = 3*newcol+30,	y1 = newrow,	x2 = 3*newcol+42,	y2 = newrow+12},
		{name = "fcrit+",	x1 = newcol+30,		y1 = 2*newrow,	x2 = newcol+42,		y2 = 2*newrow+12},
		{name = "fheal+",	x1 = 2*newcol+30,	y1 = 2*newrow,	x2 = 2*newcol+42,	y2 = 2*newrow+12},
		{name = "fdraw+",	x1 = 3*newcol+30,	y1 = 2*newrow,	x2 = 3*newcol+42,	y2 = 2*newrow+12},
		{name = "ycrit-",	x1 = newcol+60,		y1 = newrow,	x2 = newcol+72,		y2 = newrow+12},
		{name = "yheal-",	x1 = 2*newcol+60,	y1 = newrow,	x2 = 2*newcol+72,	y2 = newrow+12},
		{name = "ydraw-",	x1 = 3*newcol+60,	y1 = newrow,	x2 = 3*newcol+72,	y2 = newrow+12},
		{name = "fcrit-",	x1 = newcol+60,		y1 = newrow,	x2 = newcol+72,		y2 = 2*newrow+12},
		{name = "fheal-",	x1 = 2*newcol+60,	y1 = newrow,	x2 = 2*newcol+72,	y2 = 2*newrow+12},
		{name = "fdraw-",	x1 = 3*newcol+60,	y1 = newrow,	x2 = 3*newcol+72,	y2 = 2*newrow+12},
		{name = "enter",	x1 = 4*newcol,		y1 = 11*newrow,	x2 = 4*newcol+80,	y2 = 11*newrow+40},
		{name = "about",	x1 = 4.2*newcol,	y1 = newrow/2,	x2 = 4.2*newcol+25,	y2 = newrow/2+52}
	}
end

function input()
	love.graphics.setColor(0,255,0)
	love.graphics.print(ycrit, newcol, newrow)
	love.graphics.print(yheal, 2*newcol, newrow)
	love.graphics.print(ydraw, 3*newcol, newrow)
	love.graphics.print(fcrit, newcol, 2*newrow)
	love.graphics.print(fheal, 2*newcol, 2*newrow)
	love.graphics.print(fdraw, 3*newcol, 2*newrow)
	love.graphics.setColor(255,0,0)
	love.graphics.print(err, 4*newcol, 10*newrow-20)
	
	if (screen == 'about') then
		love.graphics.setColor(245,245,245)
		love.graphics.rectangle("fill",0,0,700,400)
		love.graphics.setColor(0,0,0)
		love.graphics.print([[
PROGRAM:

    Displays advantages of two competing trigger ratios
	Hit "c" on the keyboard to copy results to clipboard
	
ASSUMPTIONS MADE:

    No stand triggers
    Opponent lets one attack through
    No effects
    2/2/2 field
    Deck is sufficiently randomized
    Opponent guards optimally

MADE BY:

    Brampton Booster
    
    https://github.com/NanoSmasher/prob-cfvg
    bramptonbooster.wordpress.com
    bramptonbooster@hotmail.ca
    
    Copyright 2014 (c): MIT License

    THANKS FOR USING MY PROGRAM!
    ]],210,40)
	end
	
	love.graphics.setColor(255,255,255)
end

function output()
	love.graphics.setColor(255,0,0)
	love.graphics.print(string.format("%.5f", dam1), 2*newcol, 5*newrow)
	love.graphics.print(string.format("%.4f", car1), 3*newcol, 5*newrow)
	love.graphics.print(string.format("%.0f", shi1), 4*newcol, 5*newrow)
	love.graphics.print(string.format("%.5f", dam2), 2*newcol, 6*newrow)
	love.graphics.print(string.format("%.4f", car2), 3*newcol, 6*newrow)
	love.graphics.print(string.format("%.0f", shi2), 4*newcol, 6*newrow)
	love.graphics.print(string.format("%.5f", dam3), 2*newcol, 7*newrow)
	love.graphics.print(string.format("%.4f", car3), 3*newcol, 7*newrow)
	love.graphics.print(string.format("%.0f", shi3), 4*newcol, 7*newrow)
	love.graphics.print(string.format("%.5f", dam4), 2*newcol, 8*newrow)
	love.graphics.print(string.format("%.4f", car4), 3*newcol, 8*newrow)
	love.graphics.print(string.format("%.0f", shi4), 4*newcol, 8*newrow)
	love.graphics.print(string.format("%.5f", heal), newcol, 10*newrow)
	love.graphics.print(string.format("%.4f", gain), newcol, 11*newrow)
	love.graphics.setColor(255,255,255)
end

function static()
	staticcanvas = love.graphics.newCanvas(700,400)
	love.graphics.setCanvas(staticcanvas)
	staticcanvas:clear()
	love.graphics.setColor(245,245,245)
	love.graphics.rectangle("fill",0,0,700,400)

	love.graphics.setColor(0,0,0)
	love.graphics.print("# Crit Triggers", newcol, 0)
	love.graphics.print("# Heal Triggers", 2*newcol, 0)
	love.graphics.print("# Draw Triggers", 3*newcol, 0)
	love.graphics.print("Your Trigger ratios", 0, newrow)
	love.graphics.print("Your Opponents ratios", 0, 2*newrow)
	love.graphics.print("You Attack Plan", 0, 4*newrow)
	love.graphics.print("Their Defensive Plan", newcol, 4*newrow)
	love.graphics.print("Damage done", 2*newcol, 4*newrow)
	love.graphics.print("Card loss", 3*newcol, 4*newrow)
	love.graphics.print("Shield loss", 4*newcol, 4*newrow)
	love.graphics.print("R>V>R", 0, 5*newrow)
	love.graphics.print("R>V>R", 0, 6*newrow)
	love.graphics.print("V>R>R", 0, 7*newrow)
	love.graphics.print("V>R>R", 0, 8*newrow)
	love.graphics.print("Let Vanguard Through", newcol, 5*newrow)
	love.graphics.print("Let Rearguard Through", newcol, 6*newrow)
	love.graphics.print("Let Vanguard Through", newcol, 7*newrow)
	love.graphics.print("Let Rearguard Through", newcol, 8*newrow)
	love.graphics.print("Damage you heal", 0, 10*newrow)
	love.graphics.print("Cards you draw", 0, 11*newrow)
	
	love.graphics.setColor(255,255,255)
	love.graphics.draw(img_up, newcol+30, newrow)
	love.graphics.draw(img_up, 2*newcol+30, newrow)
	love.graphics.draw(img_up, 3*newcol+30, newrow)
	love.graphics.draw(img_up, newcol+30, 2*newrow)
	love.graphics.draw(img_up, 2*newcol+30, 2*newrow)
	love.graphics.draw(img_up, 3*newcol+30, 2*newrow)
	love.graphics.draw(img_dw, newcol+60, newrow)
	love.graphics.draw(img_dw, 2*newcol+60, newrow)
	love.graphics.draw(img_dw, 3*newcol+60, newrow)
	love.graphics.draw(img_dw, newcol+60, 2*newrow)
	love.graphics.draw(img_dw, 2*newcol+60, 2*newrow)
	love.graphics.draw(img_dw, 3*newcol+60, 2*newrow)
	love.graphics.draw(img_en, 4*newcol, 11*newrow)
	love.graphics.draw(img_ab, 4.2*newcol, newrow/2)
	love.graphics.setCanvas()
end