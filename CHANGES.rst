Changelog
=========


1.1 (unreleased)
----------------

- Fix wrong python_requires in setup.py. [fredvd]


1.0 (2021-12-13)
----------------

- Rebuild bundle with Plone 5.2.6:
  - plone.staticresources 1.4.4
  - Mockup 3.2.7
  [fredvd]

1.0a2 (2021-03-11)
------------------

- Fix uninstall profile to remove our resource and bundle.
  [fredvd]


1.0a1 (2021-03-09)
------------------

- Initial release. Adds inline validation and pickadage patterns in an extra bundle 
  to anonymous visitors. This is necessary when you use easyform on public websites.
  The bundle also gets merged into default.js when you run in production.
  [fredvd]
