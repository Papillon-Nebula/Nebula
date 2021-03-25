# coding: utf-8
from sqlalchemy import Column, DECIMAL, DateTime, Index, Integer, String, Text, text
from sqlalchemy.dialects.mysql import CHAR, DATETIME, MEDIUMTEXT, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Addmodule(Base):
    __tablename__ = 'addmodules'

    id = Column(Integer, primary_key=True)
    modulename = Column(String(255))
    modulenumber = Column(Integer)
    pagename = Column(String(255))
    casename = Column(String(255))


class Addyuansu(Base):
    __tablename__ = 'addyuansu'

    id = Column(Integer, primary_key=True)
    modulenumber = Column(Integer)


class Article(Base):
    __tablename__ = 'article'

    content = Column(MEDIUMTEXT)
    id = Column(Integer, primary_key=True)
    author = Column(String(255))
    title = Column(String(32))
    updatetime = Column(DateTime)


class CmsArticle(Base):
    __tablename__ = 'cms_article'
    __table_args__ = (
        Index('idx_more1', 'status', 'showApprovedTime', 'releaseFullName', 'title'),
    )

    id = Column(Integer, primary_key=True)
    title = Column(VARCHAR(200), comment='???')
    subTitle = Column(VARCHAR(200), comment='???')
    title2 = Column(VARCHAR(200), comment='?????')
    title3 = Column(VARCHAR(200), comment='??????')
    title4 = Column(VARCHAR(200), comment='??4')
    sourceId = Column(Integer, comment='????Id')
    mediaName = Column(VARCHAR(100), comment='??????')
    author = Column(VARCHAR(100), index=True, comment='????')
    keywords = Column(VARCHAR(200), comment='???')
    description = Column(VARCHAR(800), comment='??')
    editor = Column(VARCHAR(80), index=True, comment='????')
    editorEmail = Column(VARCHAR(100), comment='??Email')
    color = Column(VARCHAR(10), comment='????')
    isBlod = Column(CHAR(1), comment='????')
    isGood = Column(CHAR(1), server_default=text("'0'"), comment='????')
    articalLevel = Column(Integer, comment='????')
    type = Column(CHAR(1), comment='????\\r\\n1.????\\r\\n2.url??\\r\\n3.??\\r\\n4.??')
    status = Column(CHAR(1), server_default=text("'1'"), comment='???\\r\\n1.??(???)\\r\\n2.??\\r\\n4.???')
    releaseType = Column(CHAR(1), server_default=text("'0'"))
    resourcePath = Column(VARCHAR(1000), comment='3?2?')
    resourcePath2 = Column(VARCHAR(1000), comment='???')
    resourcePath3 = Column(VARCHAR(1000), comment='9?5?')
    resourcePath5 = Column(VARCHAR(1000), comment='3:1?')
    resourcePath6 = Column(VARCHAR(1000), comment='2:1?')
    filePath = Column(VARCHAR(300), comment='????')
    releaseFullName = Column(VARCHAR(300), nullable=False, index=True, comment='URL??')
    previewFullName = Column(VARCHAR(300), comment='??URL')
    templateId = Column(Integer, comment='??ID')
    templateName = Column(VARCHAR(50), comment='????')
    templatePath = Column(VARCHAR(1000), comment='????')
    insertedUserId = Column(Integer, index=True, comment='????ID')
    updatedUserId = Column(Integer, comment='????ID')
    deletedUserId = Column(Integer, comment='????ID')
    approvedUserId = Column(Integer, comment='????ID')
    insertedTime = Column(DATETIME(fsp=3), server_default=text("CURRENT_TIMESTAMP(3)"), comment='????')
    updatedTime = Column(DATETIME(fsp=3), server_default=text("CURRENT_TIMESTAMP(3)"), comment='????')
    deletedTime = Column(DATETIME(fsp=3), comment='????')
    approvedTime = Column(DATETIME(fsp=3), comment='????')
    showApprovedTime = Column(DATETIME(fsp=3), index=True, comment='????????')
    releaseFlag = Column(CHAR(1), comment='????\\r\\n0????\\r\\n1????')
    conType = Column(CHAR(1), comment='????\\r\\n0??\\r\\n1??\\r\\n2???')
    contributorId = Column(Integer, comment='???id')
    actionTypeId = Column(Integer, comment='??id')
    review = Column(VARCHAR(500), comment='??')
    leadTitle = Column(VARCHAR(500), comment='????')
    sayGoodCount = Column(Integer, nullable=False, server_default=text("'0'"), comment='????')
    sayBadCount = Column(Integer, nullable=False, server_default=text("'0'"), comment='????')
    mtitle = Column(VARCHAR(200), comment='?????')
    mdescription = Column(VARCHAR(800), comment='?????')
    mthumbnail = Column(VARCHAR(300), comment='??????')
    titleSeo = Column(VARCHAR(100), comment='SEO??')
    keywordsSeo = Column(VARCHAR(200), comment='SEO???')
    descriptionSeo = Column(VARCHAR(800), comment='?????')
    mark = Column(CHAR(1), server_default=text("'0'"), comment='0?????1???2???')
    conclusion = Column(VARCHAR(200), comment='??')
    resourcePath7 = Column(VARCHAR(1000), comment='1?1??')
    originalAuthor = Column(VARCHAR(100), comment='????')
    overLongTitle = Column(VARCHAR(800), comment='????')
    content_type = Column(Integer)
    content_id = Column(Integer, comment='?????id???id????id')
    style_type = Column(Integer, comment='app????????\\r\\n 1??????\\r\\n2????\\r\\n\\r\\n4?????\\r\\n5?????\\r\\n6??????\\r\\n7??????\\r\\n8??????')
    app_author_id = Column(Integer, comment='????????????id')
    sudden = Column(Integer, server_default=text("'0'"))
    price = Column(DECIMAL(18, 2), server_default=text("'0.00'"), comment='????')
    ebrungo = Column(Integer, nullable=False, server_default=text("'0'"), comment='????????')
    list_show = Column(Integer, nullable=False, server_default=text("'1'"), comment='?????????1?0?')


class CmsArticlecontent(Base):
    __tablename__ = 'cms_articlecontent'

    articleId = Column(Integer, primary_key=True)
    content = Column(MEDIUMTEXT)
    wapContent = Column(MEDIUMTEXT)
    content_charge = Column(MEDIUMTEXT)


class Testallreport(Base):
    __tablename__ = 'testallreport'

    id = Column(Integer, primary_key=True)


class Testcaseall(Base):
    __tablename__ = 'testcaseall'

    id = Column(Integer, primary_key=True)
    casestep = Column(String(255))
    modulenumber = Column(Integer)
    casedescribe = Column(String(255))
    modulename = Column(String(255))
    Usecasemethod = Column(String(255))
    Usecasefile = Column(String(255))


class User(Base):
    __tablename__ = 'users'
    __table_args__ = (
        Index('ix_id_name', 'name', 'email'),
        Index('uix_id_name', 'id', 'name', unique=True)
    )

    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False, index=True)
    email = Column(String(32), unique=True)
    password = Column(String(32), nullable=False)
    ctime = Column(DateTime)
    extra = Column(Text)
