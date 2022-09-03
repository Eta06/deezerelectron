import os
import PySimpleGUI as sg
import webbrowser
import ctypes, sys
import patoolib
import wget

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

logo = 'iVBORw0KGgoAAAANSUhEUgAAACgAAAAoCAYAAACM/rhtAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAATISURBVFhH7VjPaxxVHP+8NzO7s5vNbGJ+GTVasUooKKihCr3Yg1JUsEV70PwBnkSkePDmoYfiSSgKXtRDoaCnepPai4WgUgSjpipWI7SpzebHbrKb3dmdH36+M7NsYtbIUtjMoZ/w2e97b97O++T7472ZVUgwPDw85fv+rGEYL4dheEgplU8u9QNcMqzR/kie8zzv82q1WpILkcBisfiE1vo8mw+3x/YRATlPwcfL5fJfSjzHga/IR+RqinCZET2uJazsiOfShiOM6gtGPp9/n5174rFUQVJtTEK8xUYuGkof6pofaRUnyInAVOOOwNuFFEmYtPsC7+AkggMTUKGKGSjoqE1fff1dMquDvgtsvPQUvGdnoAMNwzcittvhO2eSWR30PcSK7hDPiajtlLFu6LtA7QGGG8JohtDNAIoUK+yGvoc4LA4AgyQRe03yL+oiXPo7bmxDzwIn7gpweNrn3XhzJnjox9annfsNqNSTif+B8O4RYHwkFpeEO/qj9RcWklkd9CzwuRkPn5xyoSWpXbKpEbgajZqBEx+E+Glp79sFx44AR5+Oc0+KhLZdLLXT7yazOug9ByWhGxZU3eRJ2aYV2yhke4PlQRoRKY1bjBlR+t3Qs8DQUwhqJoKqCZ/Wr1pskzWKZOT/DxJK8V57e9nObug5xOMO8OQBNph3UQ4m1qe4b6/72GCF7omJUWB0JNqcxePic0VxYlu//hxN2Y6eBY4NhniQeR60mH8ePdkSGvDJa24VhjIwYQzBY3A8RSa2xe/WWqxSnYNpjyJgRMN/88bv8SLb0LPAk4dbOPOiQmvNQWO1CLdUjGy1VMCbN66gqIYw6xzFBoWsaxtlnUFZ2ShxL/lh+WPowkNw7n8FrQI9NkiKJT3SP/tGskoHPeegyW/kmG62pZAzFGyh1shqSXzml1LIKBNWQlNZ9GpM+oPkPJWBonBlZNglzYRd0HsV9xk9h/ixKR/HplnJdRveVhatag4+rVvL4ouN67AZzsezB9Gg9+pk29a4K9+sXoHKjCA79CiCLEMqpOOkHYidu5Cs0sEugRkzxGSxu+abFYaP293oAEPlc4Nm9YUeSRuwX/IaDIkBh/nHU5a7Dv8RhtznaECBrr/BmFnQZgHydCXxi4pZrPTL0bv6DuwSOD3p4/zrm0lvJ177aBCH7g1w+nkWyboDd5VckSJxUF0p4NTS93BUEa86z2CTBSJFUmG+lWlXKHC+9CnUAItk6kRcGCySJo9lKZCoSD58K1mpg105yJyHY4ddaXC2eLDI1yzHVnAyGoMWaZooGPQMPWZyS8lTlK2yETMUZzHsJq0spxhubeTpxTyURWbyQDZhF+wSmDYYuVxuxwmdZ7I+MBJgccXYxYsLGRjcUIdyCn/cMnGtpPDnmsJixcditYm5rVKUb4M6j5vBJm55G1jxK1jz11H2VrHauMpcowfNHFreMlrNZfj1mEF1GeEvKXjk7xWpD/EdgbcLESg/HqUSYRhuaX7MJ/004hvx4Dmy+zvf/qJF553Vnud9FgSB/HidKlDcJdM0LxnNZnPLtu0vOTajlLqPVh7a9hPiuYt02my5XK7wXABc1y1blnWBAq/y4jjtGId56vYPXFfeqC/Tvk3PvSfiAOAfw1DvYpbuITQAAAAASUVORK5CYII='
github = 'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAKLSURBVFhHzZdLqE1RGMe3t7zfJBSSKAPyKFKGJgbChCIzA2VqwJ24d4bMJGVioEjJgIm8Bl553q4MFOVNHhNCnr//2uu7rbPPcvbe5y7xq99ZZ+2z9/rWXvvba62T/Wv6+bIuI3AmjnW1LPuAj/Gjq/0lFuI+vI8/8FfBn6jf9uMiTMYSPI/FgGVewGXYNoNQdxy726rqWo3IYKzFaLyIsUbb8RKOwUoMw6uoC1/iaXzo61X9imfwAD73x67jcCzlGFpDq3TAsxhPoY6/xduoO7uMD/AzasgP4lQ0NqC1d1wHWrEJ7eQvGHt243xZZABOyL82MBmtTbkZo2joX6Cd+AhT8R2tXT3W6KPYjnaSVGdSoGCaI8K2d2AT9zA86SlqWPuKsv8Vhm33YAOzMDxBbsRUbMNi+3OwFyVG+KOyfCCmQmuHkjqMsRWz/vqA+b40NA8ocVKhRUrrRMg8fVgHpvjSeOPLlLz3peFiWgeK73vtubsCQ31pDNGHdeCTL41pvkzJdF8aLqZ14JkvDa3nWg1ToeGekX/txcW0DnT70hiFq/OvSViPxd1XQ8zxGE6X8hameBVH4hMM29aiNREbOIfhSfIQ2ii1g5LZVtBQ7bCaWIcahRWo+XstakE6i7OxLtrKXcNicKklugnd6R1c6Wo5Sh4lyzfUxmQLtkKPrBNvYiywvIt/HFUF18ZC+wJjAWrLrYtP6EAJV7AY1NQIL8eWdKGmzkmulqMM1j6xCkcwFlzuwlK0BJ/E3a5WH23JYsEPY+U/Qsreo7jG1eoR68BerP026YIOVPJpt6TMnYtlhB14jXq7+sRSvIFqcKcOlKAOvMM9WDVvStGz0+OoMj1rziiufP8rWfYbinP48njMTLEAAAAASUVORK5CYII='
path = f'C:\\Program Files\\DeezerElectron'

layout = [[sg.Text('Deezer Electron App Installer                                      ',font=(30),background_color=('White'),text_color=('Black')),sg.Image(data=logo,size=(64,64),background_color=('White'))],
[sg.Text('by Eta06 on', text_color=('Black'),font=(10),background_color=('White')),sg.Button('',image_data=github,button_color=('White'),key=('GitHub'))],
[sg.Button('Uninstall',button_color=('Red'),size=(25,2),key='Uninstall'), sg.Button('Install',button_color=('Green'),size=(26,2),key='Install')]]

window = sg.Window('Deezer Electron Installer', layout,size=(450,180),background_color=('White'),icon=logo)

while True:
    event, values = window.read()
    isExist = os.path.exists(path)
    if event == sg.WIN_CLOSED or event == 'Cancel':
        window.close()
        break
    elif event == 'Install':
        if isExist == True:
            if is_admin():
                os.rmdir(path)
                os.mkdir(path)
                try:
                    patoolib.extract_archive("app.rar", outdir=path)
                except:
                    try:
                        wget.download('https://github.com/Eta06/deezerelectron/releases/download/v1.0.0-beta/app.rar')
                    except:
                        sg.popup('Unable to load app.rar from local and network!')
            else:
                window.close()
                ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        else:
            if is_admin():
                os.mkdir(path)
                try:
                    patoolib.extract_archive("app.rar", outdir=path)
                except:
                    try:
                        wget.download('https://github.com/Eta06/deezerelectron/releases/download/v1.0.0-beta/app.rar')
                    except:
                        sg.popup('Unable to load app.rar from local and network!')
            else:
                window.close()
                ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
                
    elif event == 'GitHub':
        webbrowser.open('https://github.com/Eta06/deezerelectron.git')
    elif event == 'Uninstall':
        if isExist == True:
            if is_admin():
                try:
                    os.rmdir(path)
                    sg.popup('Uninstalled Successfully')
                except:
                    sg.popup('Unable to remove App you can try to remove manually Path:', path)
            else:
                window.close()
                ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        else:
            sg.popup_error('App is not installed on your system!')

