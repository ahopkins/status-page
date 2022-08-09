const { description } = require('../../package')

module.exports = {
  title: 'Sample Status',
  description: description,
  head: [
    ['meta', { name: 'theme-color', content: '#3eaf7c' }],
    ['meta', { name: 'apple-mobile-web-app-capable', content: 'yes' }],
    ['meta', { name: 'apple-mobile-web-app-status-bar-style', content: 'black' }]
  ],
  base: "/status-page/",
  themeConfig: {
    repo: '',
    editLinks: false,
    docsDir: '',
    editLinkText: '',
    lastUpdated: true,
    nav: [
      {
        text: 'PacketFabric Portal',
        link: 'https://portal.packetfabric.com'
      }
    ],
    search: false,
    sidebar: null,
    componentTitles: {
      Web: "Web - API"
    }
  },
  plugins: [
    '@vuepress/plugin-back-to-top',
    '@vuepress/plugin-medium-zoom',
  ],
}
