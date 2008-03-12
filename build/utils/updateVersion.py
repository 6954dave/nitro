#!/usr/bin/env python -O 

"""
Tool used to update the version, project-wide
Add any replacement regexes here to files that include the version
"""

import os, sys, re, fileinput

if __name__ == '__main__':
    top_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
    versionFile = os.path.join(top_dir, 'VERSION')
    sequence = fileinput.input(versionFile)
    fullVersion = sequence.next().strip()
    print 'Version = %s' % fullVersion
    sequence.close()
    parts = re.match(r'(?P<major>\d+)[.](?P<minor>\d+)([-](?P<suffix>\w+))?',
                     fullVersion).groupdict()
    major, minor, suffix = parts['major'], parts['minor'], parts['suffix']
    
    #update version of C Makefiles
    makefiles = [os.path.join(top_dir, 'c/nitf/build/Makefile.in'),
                 os.path.join(top_dir, 'c/nitf.jni/build/Makefile.in'),]
    for line in fileinput.input(makefiles, inplace=1):
        line = re.sub(r'(\s*MAJOR_VERSION\s*=\s*)\d+', r'\g<1>%s' % major, line)
        line = re.sub(r'(\s*MINOR_VERSION\s*=\s*)\d+', r'\g<1>%s' % minor, line)
        line = re.sub(r'(\s*VERSION_SUFFIX\s*=\s*).+', r'\g<1>%s' % suffix or '', line)
        sys.stdout.write(line)
    
    #update java properties file
    propsFile = os.path.join(top_dir, 'java/nitf/project.properties')
    for line in fileinput.input(propsFile, inplace=1):
        line = re.sub(r'(\s*version\s*=\s*).+', r'\g<1>%s' % fullVersion.lower(), line)
        sys.stdout.write(line)
    
    #update python setup.py
    setupFile = os.path.join(top_dir, 'python/nitf/setup.py')
    for line in fileinput.input(setupFile, inplace=1):
        line = re.sub(r'(\s*version\s*=\s*).+', r"\g<1>'%s'" % fullVersion.lower(), line)
        sys.stdout.write(line)
    
    #update windows installer
    setupFile = os.path.join(top_dir, 'build/installer/nitro_installer.iss')
    for line in fileinput.input(setupFile, inplace=1):
        line = re.sub(r'\d+[.]\d+[-]setup', r'%s-setup' % fullVersion.lower(), line)
        line = re.sub(r'\d+[.]\d+(?![-]setup)([-]\w+)?', r'%s' % fullVersion, line)
        line = re.sub(r'\d+[.]\d+.+[-]setup', r'%s-setup' % fullVersion.lower(), line)
        #line = re.sub(r'\d+[.]\d+((?![-]setup)[-]\w+)?-setup', r'%s-setup' % fullVersion.lower(), line)
        
        
        sys.stdout.write(line)
    
    