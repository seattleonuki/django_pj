# from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.views.generic import DetailView
from manager.models import Manager, Company, Employee


# ログイン画面操作
def index(request) :
    """
    管理者ログインページ
    """
    # 認証しているかどうかのロジック（if）

    # postメソッドの場合の条件分岐しないと多分エラー治らない（emailエラー（MultiValueDictKeyError））

    if (request.method == 'POST') :

        mail = request.POST['email']
        pwd = request.POST['password']
        
        try :
            if (mail == '' or pwd == '') :
                raise Exception('フォームを入力してください。')

            if (not Manager.objects.filter(email = mail) or not Manager.objects.filter(password = pwd)) :
                raise Exception('メールアドレスまたはパスワードが違います。')

            elif (Manager.objects.filter(email = mail) and Manager.objects.filter(password = pwd)) :

                data = {
                    'users' : Company.objects.all().order_by('id'),
                }
                return render(request, 'home.html', data)

        except Exception as e :
            message = e
            return render(request, 'login.html', { 'message' : message })


def login(request) :
    return render(request, 'login.html')


# 管理者アカウント操作
def newAcc(request) :
    """
    管理者アカウント作成ページ遷移
    """
    return render(request, 'newAcc.html')


def registerAccount(request) :
    """
    管理者アカウント作成
    """

    email = request.POST['email']
    password = request.POST['password']
    conf_password = request.POST['conf_password']

    password_length = 4

    # def strength_password(password) :
    #     require_pass_elements = re.search(re.compile(r'^[a-zA-Z0-9]+$'), password)
    #     if ()

    try :
        if (email == '') :
            raise Exception('メールアドレスを入力してください。')
        
        if (password == '') :
            raise Exception('パスワードを入力してください。')

        if (conf_password == '') :
            raise Exception('確認用パスワードを入力してください。')

        if (len(password) < password_length) :
            raise Exception('パスワードは{}文字以上で入力してください。'.format(password_length))

        if not(password == conf_password) :
            raise Exception('パスワードが一致しません。')

        if (Manager.objects.all().filter(email = email)) :
            raise Exception('既存のアカウント名です。')

        # パスワード要件バリデーション（半角英数字）
        # if

        else :
            # salt = 
            Manager.objects.create(email=email, password=password, is_active=True)
            return render(request, 'register_account.html')

    except Exception as e :
        message = e
        return render(request, 'newAcc.html', { 'message' : message })



def resetPass(request) :
    return render(request, 'forgetPass.html')


def logOut(request) :
    return render(request, 'logged_out.html')


# 企業アカウント操作
def add(request) :
    """
    企業アカウント作成
    """
    company_name = request.POST['name']
    password = request.POST['password']

    try :
        if (company_name == '' or password == '') :
            raise Exception('アカウント名とパスワードは必須項目です。')

        if (company_name == '') :
            raise Exception('アカウント名がすでに存在しています。')
        
        else :
            Company.objects.create(name=company_name, password=password, is_active=True)
            data = {
                'users' : Company.objects.all().order_by('id'),
            }
            return render(request, 'home.html', data)

    except Exception as e :
        register_error = e
        return render(request, 'home.html', { 'register_error' : register_error })


def delete_company(request) :
    """
    企業アカウント削除
    """
    # Company.objects.filter().delete()

    data = {
        'users' : Company.objects.all().order_by('id')
    }
    return render(request, 'home.html', data)


def update_company(request) :
    """
    企業アカウント更新
    """
    # Company.objects.filter().update()

    data = {
        'users' : Company.objects.all().order_by('id')
    }
    return render(request, 'home.html', data)


def employees_detail(request) :
    """
    企業リンクから従業員リストへの画面遷移
    """
    id = request.GET['param']
    data = {
        'employees' : Employee.objects.all().filter(company_id=id).order_by('id')
    }
    return render(request, 'emp_detail.html', data)


# 支払
def payment(request) :
    return render(request, 'payment.html')


def finished_pay(request) :
    return render(request, 'finished_pay.html')


# 登録
def apply_info(request) :

    data = {
        'employees' : Employee.objects.all().order_by('id')
    }
    return render(request, 'apply_info.html', data)

def apply_result(request) :

    data = {
        'employees' : Employee.objects.all().order_by('id')
    }
    return render(request, 'apply_result.html', data)