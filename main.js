// noinspection JSIgnoredPromiseFromCall
const { app, BrowserWindow } = require('electron');

app.disableHardwareAcceleration()
let notsplash = false;

const createWindow = () => {

    const win = new BrowserWindow({
        titleBarStyle: 'hidden',
        trafficLightPosition: { x: 10, y: 10 },
      width: 1120,
      height: 610,
      minHeight: 600,
      minWidth: 800,
      show: false,
      webPreferences:{nodeIntegration:true},
      icon: __dirname + "/icon.png",
      opacity: 0.98,
    })
    let splash = new BrowserWindow({
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
        {userAgent: 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36 Ubuntu/22.04'});
    if (notsplash){
      console.log('Not executed');
    }else {
    win.webContents.on('did-finish-load', function() {
        splash.hide()
	      win.show();
        notsplash = true;

  });
  win.on('close', function() {
    app.quit();
  })

}
}

app.whenReady().then(() => {
createWindow()
})
