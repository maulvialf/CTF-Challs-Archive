const {app, BrowserWindow} = require('electron')
const path = require('path')
const url = require('url')

let window = null



// Wait until the app is ready
app.once('ready', () => {
  // Create a new window
  window = new BrowserWindow({
    // Don't show the window until it ready, this prevents any white flickering
    show: false,
    title: "5Head",
    // Make the window transparent
    transparent: true,
    // Remove the frame from the window
    frame: false,
    
  })

  // Load a URL in the window to the local index.html path
  window.loadURL(url.format({
    pathname: path.join(__dirname, 'index.html'),
    protocol: 'file:',
    slashes: true
  }))

  // Show window when page is ready
  window.once('ready-to-show', () => {
    window.maximize()
    window.show()
  })
})
