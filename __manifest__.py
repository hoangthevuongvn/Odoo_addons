{
    'name': "Trial Report",
    'name_vi_VN': "Báo cáo thử việc",

    'summary': """
probationary employee report""",
    'summary_vi_VN': """
Phiếu báo cáo tình trạng công việc dành cho nhân viên thử việc
""",

    'description': """
What it does
============
Long description of module's purpose

Key Features
============
1. Feature 1

   * Sub-Feature 1
   * Sub-Feature 2

     * Sub-sub-feature 1
     * Sub-sub-feature 2

2. Feature 2

   * Sub-Feature 1
   * Sub-Feature 2

Editions Supported
==================
1. Community Edition
2. Enterprise Edition

    """,

    'description_vi_VN': """
Ứng dụng này làm gì
===================
Mô tả chi tiết về module

Tính năng chính
===============
1. Tính năng 1

   * Tính năng Phụ 1
   * Tính năng Phụ 2

     * Tính năng Phụ Chi tiết 1
     * Tính năng Phụ Chi tiết 2

2. Tính năng 2

   * Tính năng Phụ 1
   * Tính năng Phụ 2

Ấn bản được Hỗ trợ
==================
1. Ấn bản Community
2. Ấn bản Enterprise

""",

    'author': "Viindoo",
    'website': "https://viindoo.com",
    'live_test_url': "https://v14demo-int.viindoo.com",
    'live_test_url_vi_VN': "https://v14demo-vn.viindoo.com",
    'support': "apps.support@viindoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr',],

    # always loaded
    'data': [
        'security/trial_report.xml',
        'security/ir.model.access.csv',
        'views/form_views.xml',
        'views/tree_views.xml',
        'views/menu_action_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'images' : [
        # 'static/description/main_screenshot.png'
        ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'price': 99.9,
    'currency': 'EUR',
    'license': 'OPL-1',
}
