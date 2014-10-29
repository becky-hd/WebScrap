var casper = require('casper').create({
  waitTimeout: 15000,
  stepTimeout: 15000,
  verbose: true,
  logLevel: 'info',
 pageSettings: {
    "userAgent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.10 (KHTML, like Gecko) Chrome/23.0.1262.0 Safari/537.10',
    "loadImages": false,
    "loadPlugins": false,
    "webSecurityEnabled": false,
    "ignoreSslErrors": true,
  },
  onWaitTimeout: function() {
    casper.echo('Wait TimeOut Occured');
  },
  onStepTimeout: function() {
    casper.echo('Step TimeOut Occured');
  }
}); 
var url = "http://www.jide123.net/manhua/7081/168416.html?p="; 

casper.start();
var result = [];
for (var i = 2; i < 196; i++)
{ 
	var sitelink = url+i;
	casper.thenOpen(sitelink, function() {
		this.echo('Get URL ' + sitelink + ' ------->> Site current URL ------>> ' + this.getCurrentUrl() + '\n');
	});
	casper.then(function(){
		var images = this.evaluate(function() {
			var scripts = document.querySelectorAll('img[name="qTcms_pic"]');
				return Array.prototype.map.call(scripts, function (e) {
					return e.getAttribute('src');
			});
		});
	result.push(images);
	this.echo("url = " + images + ", len= "+result.length);
	}); 
} // end for loop

casper.then(function(){
	var fs = require("fs");
	var img = "osamu8.urls.log";
	fs.write(img, result.join("\n"), 'w');
	});
	
casper.run();

