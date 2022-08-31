SERVICE_URL = 'https://symphony-solutions.com/'
WRONG_URL_HTTPS = ['http://symphony-solutions.com',
                   'http://symphony-solutions.com',
                   'http://www.symphony-solutions.com', ]

XML_URL = 'https://symphony-solutions.com/sitemap.xml'

ALL_URL_LIST = ['insights',
                'services/digital-marketing-orchestration',
                'privacy-policy',
                'contact-us',
                'approaches/agile-driven',
                'approaches/managed-product-development',
                'sitemap',
                'approaches/dedicated-team',
                'company',
                'services/design',
                'services/quality-assurance-and-testing',
                'services/mobile-application-development',
                'services/service-design',
                'services/i-gaming-solutions',
                'services/agile-transformation',
                'services/custom-software-development',
                'services/business-agility',
                'services/agile-consulting-and-coaching',
                'services/agile-implementation',
                'services/agile-training-and-certification',
                'services/agile-assessment',
                'insights/igb',
                'leading-safe-5-0-registration',
                'thank-you-for-submission',
                'igaming/esports',
                'igaming/ai-driven-content-personalization',
                'igaming/integration-services',
                'services/omnichannel-orchestration',
                'launch-your-product-acceleration-teams',
                'services/education',
                'services/application-modernization',
                'services/devops',
                'services/cloud-native-development',
                'services/cloud-solutions',
                'services/application-assessment',
                'services/cloud-managed-services',
                'industries/healthcare-software-development',
                'igaming/software-development',
                'awards-and-partners',
                'enhance-your-online-experience',
                'industries/casino-game-development',
                'corporate-social-responsibility',
                'corporate-social-responsibility/corporate-volunteering',
                'corporate-social-responsibility/empowering-communities',
                'corporate-social-responsibility/education-and-learning',
                'corporate-social-responsibility/go-green',
                'industries/custom-elearning-software-development',
                'launch-your-product-acceleration-teams',
                'insights/symphony-solutions-supports-national-rehabilitation-center-of-ukraine',
                'cases/helping-product-grow-with-managed-services',
                'insights/symphony-solutions-acquires-iso-certificate',
                'cases/improving-data-accuracy-with-gtm-server-side-implementations',
                'insights/data-science-in-igaming',
                'cases/team-augmentation-on-nigerian-market',
                'insights/data-engineering-best-practices',
                'cases/creating-best-experience-through-improved-ux-ui',
                'cases/building-centralized-data-management-solution-for-igaming',
                'insights/vivino-client-review-for-symphony-solutions',
                'insights/how-technology-puts-the-care-in-healthcare',
                'insights/cloud-migration-risks-and-mitigation',
                'insights/legacy-application-modernization-strategies',
                'insights/spoedtestcorona-mentioned-in-fastcompany-world-changing-ideas-awards-2022',
                'insights/symphony-solutions-shortlisted-for-egr-b2b-awards-2022',
                'insights/cloud-managed-services-for-business',
                'insights/symphony-solutions-supports-ukraine',
                'cases/cloud-managed-services-for-igaming-platform',
                'insights/symphony-solutions-to-attend-ice-london-2022',
                'cases/designing-solution-for-online-covid-1self-testing',
                'insights/symphonians-volunteer-for-ukraine',
                'cases/developing-unique-player-experience',
                'cases/betting-and-gaming-solution-for-african-markets',
                'insights/stand-with-ukraine',
                'insights/cloud-transformation-in-healthcare',
                'insights/mobile-gambling-in-africa',
                'insights/cloud-software-development-guide',
                'insights/software-developer-hiring-process',
                'insights/wining-health-tech-digital-award-2021',
                'insights/agile-implementation-guide',
                'insights/cloud-readiness-assessment-checklist',
                'insights/mobile-game-design-in-igaming',
                'insights/symphony-solutions-among-finalists-in-app-developer-awards-2021',
                'insights/elearning-app-development-types-features-technologies',
                'cases/designing-pwa-app-for-mental-health',
                'insights/distributed-agile-team-management',
                'insights/we-take-part-in-ice-connect-virtual-summit',
                'insights/cybersecurity-in-igaming-overview',
                'insights/custom-lms-development-for-enterprise',
                'insights/scrum-master-competencies',
                'cases/removing-security-vulnerabilities-for-marketing-firm',
                'insights/agile-metrics-that-matter',
                'insights/cloud-native-technologies-in-healthcare-overview',
                'insights/symphony-solutions-shortlisted-for-egr-b2b-awards-2021',
                'cases/delivering-relevant-content-across-slower-networks',
                'insights/top-it-services-providers-in-poland',
                'cases/integrated-mobile-application-for-fleet-management',
                'insights/cloud-computing-scalability',
                'insights/symphony-solutions-breaks-into-top-10-outsourcing-companies-in-ukraine-according-to-clutch',
                'insights/cybersecurity-in-igaming-secure-by-design',
                'insights/symphony-solutions-delivers-in-record-time-btg-solution-to-the-company-specialized-in-covid-testing-for-the-dutch-government',
                'insights/leveraging-cloud-native-technologies-in-healthcare-to-respond-to-urgent-social-needs',
                'cases/leveraging-serverless-capabilities-to-build-a-mental-health-application',
                'insights/agile-team-structure-in-software-development',
                'insights/sportsbook-platform-development-comparison-guide',
                'insights/benefits-of-cloud-computing-in-healthcare',
                'insights/building-agile-transformation-roadmap',
                'insights/symphony-solutions-payments-optimization-and-integration-project-for-ladbrokes-coral',
                'insights/clutch-ranks-symphony-solutions-among-western-europes-top-b2b-firms-for-2021',
                'insights/csr-annual-report-essential-part-of-company-focus-in-2020',
                'insights/how-to-make-your-agile-transformation-process-right-tips-from-experience-with-multiple-clients',
                'insights/symphony-solutions-rated-as-top-it-employer-in-2020-by-dou',
                'cases/agile-transformation-for-cross-functional-teams',
                'insights/symphony-solutions-listed-among-top-web-development-companies-in-the-usa',
                'insights/symphony-solutions-joins-the-project-to-provide-affordable-covid-19-testing',
                'insights/10-benefits-of-service-design-for-product-launch',
                'insights/agile-mindset-to-drive-your-business-results',
                'insights/safe-5-0-product-owner-product-manager-certification-course',
                'insights/from-agile-coach-to-taking-on-the-coo-role',
                'cases/apc-helps-pharmaceutical-companies-speed-release-of-life-changing-medicines',
                'cases/accelerating-mvp-for-covid-19-testing-app-using-aws-cloud-platform',
                'insights/igaming-industry-tech-trends-for-2021',
                'insights/the-way-we-live-the-way-we-work-now',
                'insights/symphony-solutions-achieves-select-consulting-partner-status-in-aws-partner-network',
                'cases/sportsbook-betting-platform-performance-improvement-for-ladbrokes-coral',
                'insights/symphony-solutions-recognized-as-top-cloud-consulting-company-in-2020',
                'insights/lean-agile-service-design-practical-workshop',
                'insights/say-no-more-to-domestic-violence',
                'insights/qa-approach-and-best-practices',
                'cases/omnichannel-approach-for-italian-software-house',
                'cases/omnichannel-solution-to-make-testing-for-covid-19-fast-and-safe',
                'cases/your-loyalty-is-our-biggest-asset',
                'insights/agile-fundamentals-online-training',
                'insights/agile-basics-online-course',
                'cases/plm-solutions-for-life-science',
                'cases/knowledge-solutions-platform-for-global-industry-leaders',
                'cases/slot-game-design-and-digital-experiences',
                'insights/how-to-increase-customer-engagement-and-loyalty',
                'insights/vivino-app-a-digital-wine-experience',
                'insights/lean-agile-service-design-webinar',
                'cases/omp-supply-chain-management',
                'insights/quarantine-2020',
                'insights/krakow-moving-office',
                'insights/igb-webinar-on-ai-driven-hyper-personalisation',
                'cases/smart-product-recommendations-and-personalisation-with-ai',
                'insights/artificial-intelligence-an-overview',
                'cases/rapid-scaling-in-new-market',
                'cases/b2b-marketplace-with-supply-chain-automation',
                'cases/60-less-steps-improves-conversion-rate',
                'cases/vivino-becomes-the-most-downloaded-wine-app-in-the-world',
                'insights/igaming-business-webinar',
                'insights/ai-driven-hyper-personalized-recommendations',
                'insights/leading-safe-in-malta',
                'insights/igaming-business-webinar-on-driving-casino-yield-with-ai-technologies',
                'insights/white-paper-how-service-design-can-help-bring-offline-users-online',
                'cases/reinforced-learning-with-mindmarker',
                'cases/hybrid-cloud-environment-aws-azure',
                'insights/symphony-solutions-on-ft-1000-list-for-2020',
                'insights/clutch-speaks-loud-and-strong-for-symphony-solutions',
                'insights/online-pi-planning-for-distributed-teams',
                'cases/a-new-face-always-gets-noticed',
                'cases/new-sportsbook-platform-increases-user-preference',
                'insights/leading-safe-4-6-amsterdam',
                'insights/lean-agile-service-design-workshop',
                'cases/ai-and-igaming-come-together',
                'cases/vr-game-increases-awareness',
                'cases/increasing-ivf-odds-with-ai',
                'insights/igaming-industry-in-the-time-of-covid-19',
                'insights/service-design-thinking',
                'cases/salesforce-retail-banking',
                'insights/serverless-architecture',
                'insights/leading-safe-5-0-antwerp',
                'insights/safe-partner',
                'insights/igb-affiliate-london',
                'insights/symphony-solutions-to-attend-ice-london-2020',
                'insights/newest-sportsbook-platform-delivered-to-ladbrokes-coral',
                'insights/symphony-solutions-attends-sigma19-in-malta',
                'insights/write-code-like-music-welcome-to-symphony-solutions',
                'insights/symphony-solutions-among-the-20-most-promising-devops-solution-providers-of-2019',
                'insights/symphony-solutions-is-excited-to-be-on-clutch-as-a-top-software-developer',
                'insights/symphony-solutions-comes-to-boston',
                'insights/172nd-grand-national-a-remarkable-experience',
                'cases/new-product-releases-every-2-weeks',
                'cases/agile-transformation-doubles-release-time',
                'cases/product-development-increases-user-base',
                'cases/cloud-engineering-increases-security',
                'cases/agile-transformation-grows-revenue',
                'insights/how-a-dutchman-opened-an-it-business-in-ukraine',
                'insights/silicon-review-names-symphony-solutions-among-the-50-best-workplaces-of-2018',
                'insights/symphony-solutions-among-insights-success-20-most-admired-companies-to-watch-in-2018',
                'insights/new-partnership-and-a-delivery-center-in-the-heart-of-krakow',
                'insights/symphony-solutions-among-50-best-workplaces-of-2017-by-cio-bulletin',
                'insights/agile-transformation-company-of-2017-award',
                'insights/symphony-solutions-became-a-google-partner',
                'insights/we-are-at-20-most-promising-quality-assurance-solution-providers-2016',
                'insights/symphony-solutions-launched-a-new-office-in-macedonia',
                'insights/we-are-at-20-most-promising-java-development-solution-providers',
                'insights/symphony-solutions-opened-a-new-office-in-rzeszow', ]
