/** @type {import('next').NextConfig} */

const nextConfig = {
  experimental: {
    appDir: true,
  },
  reactStrictMode:true,
  env:{
    NEXT_PUBLIC_PORT: process.env.NEXT_PUBLIC_PORT,
  }
}

module.exports = nextConfig