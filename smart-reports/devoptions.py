from database import db_session
from models import test_metadata
from sqlalchemy import Column, Integer, String, DateTime, Float

#db_session.commit()
#Esto básicamente lee todo de la clase test_metadata 
test_metadata.query.all()


#for instance in db_session.query(test_metadata):
#   print(instance.date, instance.flag)



#Este código te la sopla de momento, ves abajo a get_js_calendardatasource. Todo esto es temporal
def  get_js_maincalendar():
    jsstring=jsstring= """
    function editEvent(event) {
	    $('#event-modal input[name="event-index"]').val(event ? event.id : '');
	    $('#event-modal input[name="event-name"]').val(event ? event.name : '');
	    $('#event-modal input[name="event-location"]').val(event ? event.location : '');
	    $('#event-modal input[name="event-start-date"]').datepicker('update', event ? event.startDate : '');
	    $('#event-modal input[name="event-end-date"]').datepicker('update', event ? event.endDate : '');
	    $('#event-modal').modal();
    }

    function deleteEvent(event) {
	    var dataSource = $('#calendar').data('calendar').getDataSource();

	    for(var i in dataSource) {
		    if(dataSource[i].id == event.id) {
			    dataSource.splice(i, 1);
			    break;
		    }
	    }
	
	    $('#calendar').data('calendar').setDataSource(dataSource);
    }

    function saveEvent() {
	    var event = {
		    id: $('#event-modal input[name="event-index"]').val(),
		    name: $('#event-modal input[name="event-name"]').val(),
		    location: $('#event-modal input[name="event-location"]').val(),
		    startDate: $('#event-modal input[name="event-start-date"]').datepicker('getDate'),
		    endDate: $('#event-modal input[name="event-end-date"]').datepicker('getDate')
	    }
	
	    var dataSource = $('#calendar').data('calendar').getDataSource();

	    if(event.id) {
		    for(var i in dataSource) {
			    if(dataSource[i].id == event.id) {
				    dataSource[i].name = event.name;
				    dataSource[i].location = event.location;
				    dataSource[i].startDate = event.startDate;
				    dataSource[i].endDate = event.endDate;
			    }
		    }
	    }
	    else
	    {
		    var newId = 0;
		    for(var i in dataSource) {
			    if(dataSource[i].id > newId) {
				    newId = dataSource[i].id;
			    }
		    }
		
		    newId++;
		    event.id = newId;
	
		    dataSource.push(event);
	    }
	
	    $('#calendar').data('calendar').setDataSource(dataSource);
	    $('#event-modal').modal('hide');
    }

    $(function() {
	    var currentYear = new Date().getFullYear();

	    $('#calendar').calendar({ 
		    enableContextMenu: true,
		    enableRangeSelection: true,
		    contextMenuItems:[
			    {
				    text: 'Update',
				    click: editEvent
			    },
			    {
				    text: 'Delete',
				    click: deleteEvent
			    }
		    ],
		    selectRange: function(e) {
			    editEvent({ startDate: e.startDate, endDate: e.endDate });
		    },
		    mouseOnDay: function(e) {
			    if(e.events.length > 0) {
				    var content = '';
				
				    for(var i in e.events) {
					    content += '<div class="event-tooltip-content">'
									    + '<div class="event-name" style="color:' + e.events[i].color + '">' + e.events[i].name + '</div>'
									    + '<div class="event-location">' + e.events[i].location + '</div>'
								    + '</div>';
				    }
			
				    $(e.element).popover({ 
					    trigger: 'manual',
					    container: 'body',
					    html:true,
					    content: content
				    });
				
				    $(e.element).popover('show');
			    }
		    },
		    mouseOutDay: function(e) {
			    if(e.events.length > 0) {
				    $(e.element).popover('hide');
			    }
		    },
		    dayContextMenu: function(e) {
			    $(e.element).popover('hide');
		    },
            style:'background',
		    dataSource: [""" + get_js_calendardatasource() + """]
	    });
	    $('#save-event').click(function() {
		    saveEvent();
	    });
    });
    """
    return jsstring


#https://docs.sqlalchemy.org/en/latest/
# VERSION NUESTRA 1.2.10
# aquí un pequeño comentario:
# Esto genera solo texto plano que es interpretado por el explorador y js
# lo único de alchemy es acceder a la clase test_metadata y como está llena con los datos de la tabla
# crea la cadena co esa info.
# supongo que si usas nombres en inglés funcionará para los flags mas comunes red, green, yellow

def get_js_calendardatasource():
    calendardatasource=""
    counter=0
    for instance in db_session.query(test_metadata):
        if counter==0:
            registry="{id:" + str(counter) + ",name: '" + str(instance.size) + "',color: '" +str(instance.flag)+ "', startDate: new Date("+str(instance.date.year)+","+str(instance.date.month)+","+str(instance.date.day)+"), endDate: new Date("+str(instance.date.year)+","+str(instance.date.month)+","+str(instance.date.day)+")}"
        else:
            registry=",{id:" + str(counter) + ",name: '" + str(instance.size) + "',color: '" +str(instance.flag)+ "', startDate: new Date("+str(instance.date.year)+","+str(instance.date.month)+","+str(instance.date.day)+"), endDate: new Date("+str(instance.date.year)+","+str(instance.date.month)+","+str(instance.date.day)+")}"
        #te lo dedico CO
        counter=counter+1 
        calendardatasource=calendardatasource+registry
    return calendardatasource












