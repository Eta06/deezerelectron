
const { app, BrowserWindow, electron } = require('electron')

const path = require('path');
const client = require('discord-rich-presence')('1014256106173906944');
app.disableHardwareAcceleration()
var os = require('os');
var win = null;
var splash= null;
var notsplash = false;



const createWindow = () => {
  
    const win = new BrowserWindow({
      width: 1000,
      height: 610,
      minHeight: 600,
      minWidth: 800,
      show: false,
      webPreferences:{nodeIntegration:true},
      icon: __dirname + "/icon.png",
      opacity: 0.97,
    })
    var splash = new BrowserWindow({ 
      width: 800, 
      height: 600, 
      transparent: true, 
      frame: false, 
      alwaysOnTop: true,
      show: true,
      icon: __dirname + "/icon.png",
    });
    require("@electron/remote/main").initialize();
    require("@electron/remote/main").enable(splash.webContents);
    splash.loadFile('splash.html');
    splash.center();
    win.removeMenu()
    win.loadURL('https://deezer.com/',
    {userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'});
    if (notsplash == true){
      console.log('Not executed');
    }else {
    win.webContents.on('did-finish-load', function() {
        splash.hide()
	      win.show();
        var notsplash = true;
      
  });  
  win.on('close', function() {
    app.quit();
  })
  
}

}




client.updatePresence({
  state: 'Deezer Electron',
  details: 'Listening on',
  startTimestamp: Date.now(),
  largeImageKey: 'icon',
  smallImageKey: 'icon',
  instance: true,
});




app.whenReady().then(() => {

createWindow()
})
