import '../styles/globals.modules.css' 
 
export default function RootLayout({ children }) {
 return (
    <html lang="en">
      <head>
        <title>XV-invitation</title>
      </head>
      <body>
        {children}
      </body>
    </html>
  )
}
