class BaseGenerate():
    def update(self):
        print('update starting')


class Sphere(BaseGenerate):
    sph = {i: s for i, s in enumerate([
        'общегосударственные',
        'оборона',
        'безопасность',
        'экономика',
        'жкх',
        'окружающей',
        'образование',
        'культура',
        'здравоохранение',
        'социальная',
        'спорт'])}
    sph_i = {i: s for i, s in enumerate([
        'B-S-government',
        'B-S-national_defence',
        'B-S-national_security',
        'B-S-national_economy',
        'B-S-housing_utilities',
        'B-S-environment',
        'B-S-education',
        'B-S-culture',
        'B-S-health',
        'B-S-social_policy',
        'B-S-pe_and_sports',
        'B-S-mass_media',
        'B-S-national_debt',
        'B-S-transferts_to_subjects',
        'B-S-unidentified',
        'B-S-approved',
    ])}

    def update(self, sphere, sphere_code):
        self.sph[len(self.sph)] = sphere
        self.sph_i[len(self.sph_i)] = sphere_code


class Theme_q(BaseGenerate):
    main_t = {1: 'дефицит', 2: 'поступления', 3: 'траты'}
    main_t_i = {1: '|D ', 2: '|R ', 3: '|S '}

    def update(self, theme, theme_code):
        self.main_t[len(self.main_t)] = theme
        self.main_t_i[len(self.main_t_i)] = theme_code
